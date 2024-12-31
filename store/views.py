from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import SignUpForm, UpdateUserForm , ChagePasswordForm , UserInfoForm,ContactForm
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,  EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(
            Q(name__icontains=searched) | 
            Q(description__icontains=searched)| 
            Q(author__icontains=searched))
        if not searched:
            messages.error(request,"There is no such a product, please try again. ")
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})


def update_info(request):
    if request.user.is_authenticated:
        current_users = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_users)
        if form.is_valid():
            form.save()
            messages.success(request, "Yoor info has been updated..")
            return redirect('home')
        return render(request, 'update_info.html', {"form":form})


def update_password(request):
    if request.user.is_authenticated:
        current_user= request.user
        if request.method == "POST":
            form = ChagePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, " You have changed your password")
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('update_password')
        else:
            form = ChagePasswordForm(current_user)
            return render(request, 'update_password.html', {'form':form})
    else:
        messages.success(request, 'You must log in ')
        return redirect('login')



def update_user(request):
    if request.user.is_authenticated:
        current_users = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_users)
        if user_form.is_valid():
            user_form.save()
            login(request, current_users)
            messages.success(request, "User Profile has been updated..")
            return redirect('home')
        return render(request, 'update_user.html', {"user_form":user_form})


def category(request,space):
    space = space.replace ('-', ' ')

    try:
        category= Category.objects.get(name=space)
        products = Product.objects.filter(category=category)
        paginator = Paginator(products, 8)  # Show 8 products per page

        page_number = request.GET.get('page')  # Get current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the corresponding page
        return render(request, 'category.html', {"products": page_obj, 'category':category})
    except:
        messages.success(request,('That Category does not exist'))
        return redirect('home')

def product(request,pk):
    product= Product.objects.get(id=pk)
    return render(request, 'product.html', {"product": product})


def download_pdf(request, pdf_id):
    if request.user.is_authenticated:
        try:
            pdf = Product.objects.get(id=pdf_id)
        except Product.DoesNotExist:
            messages.error(request, "The requested file does not exist.")
            return redirect('home')
        if not pdf.file or not pdf.file.name:
            messages.error(request, "The requested file is not available.")
            return redirect('home')
        response = HttpResponse(pdf.file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{pdf.file.name}"'
        messages.success(request,"Good!!!your book has already downloaded.Check in your download folder")   
        return response
    else:
        messages.error(request, "Please register first🥰, if you did already, please log in to download the file...😉")
        form = SignUpForm()
        return render(request, "register.html", {'form': form})


def home(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 8)  # Show 8 products per page

    page_number = request.GET.get('page')  # Get current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the corresponding page

    return render(request, 'home.html', {'products': page_obj})

def about(request):
    return render(request, 'about.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,(f"Hi!!{user}..You have logged in successfully!!"))
            return redirect ('home')
        else:
            messages.success(request,(f'Hi!!{user}..Please check User Name and Password again'))
            return redirect ('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out.."))
    return redirect ('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Hi!!!{user}....You have signed up successfully.')
                    return redirect('update_info')
                else:
                    messages.error(request, 'User authentication failed after registration.')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            print(form.errors)  # Debug: Print the validation errors
            messages.error(request, 'There was a problem with your registration. Please try again.')
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})


@receiver(post_save, sender=Product)
def send_newsletter(sender,instance,created,**kwargs):
    if created:
        logged_in_users  = User.objects.filter(is_active=True).exclude(email__exact="")
        subject = f"New Update: {instance.name}"
        for user in logged_in_users:
            if user.is_authenticated and user.profile.is_subscriber:
                message = render_to_string('newsletter.html', {'news': instance, 'user': user})
                send_mail(
                subject,
                message,
                'zinkolaymgy@gmail.com',  # Replace with your sender email
                [user.email],  # Recipient's email
                fail_silently=False,
            )

@login_required
def subscribe(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.is_subscriber = True
        profile.save()
        messages.success(request, f'Hi!!{profile}. Thanks for your Subscription!')
        return redirect('home')  # Redirect to the desired page
    return redirect('home')


@login_required
def unsubscribe(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        profile.is_subscriber = False
        profile.save()
        messages.success(request, f"Hi!!{profile}.You have unsubscribed the channel, to get more information about any update on our channel, we suggest to subscribe..")
        return redirect('home')  # Redirect to the desired page
    return redirect('home')

# views.py



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            customer_email = form.cleaned_data['customer_email']
            message = form.cleaned_data['message']
            
            # Construct email
            subject = f"Contact Form Submission from {name}"
            full_message = f"Message from {name} ({customer_email}):\n\n{message}"
            
            send_mail(
                subject,
                full_message,
                customer_email,  # From email
                ['zinkolaymgy@gmail.com'],  # To email(s)
            )
            
            messages.success(request, f'Hi {name}Your message has been sent successfully!')
            form = ContactForm()  # Reset the form
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
