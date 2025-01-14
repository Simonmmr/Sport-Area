from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from .forms import ContactForm,PostForm
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(
            Q(title__icontains=searched) | 
            Q(subtitle__icontains=searched))
        if not searched:
            messages.error(request,"There is no such a topic, please try again. ")
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})


def category(request,space):
    space = space.replace ('-', ' ')

    try:
        category = get_object_or_404(Category, name=space)
        products = Product.objects.filter(category=category).order_by('id')
        paginator = Paginator(products, 6)  # Show 8 products per page

        page_number = request.GET.get('page')  # Get current page number from the URL
        page_obj = paginator.get_page(page_number)  # Get the corresponding page
        return render(request, 'category.html', {"products": page_obj, 'category':category})
    except:
        messages.success(request,('That Category does not exist'))
        return redirect('home')

def home(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 9)  # Show 9 products per page

    page_number = request.GET.get('page')  # Get current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the corresponding page

    return render(request, 'home.html', {'products': page_obj})

def view_detail(request,pk):
    product= Product.objects.get(id=pk)
    return render(request, 'view_detail.html', {"product": product})

def edit_post(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=pk)
    form = PostForm(request.POST or None, instance=product)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('view_detail', pk=product.id)  # Redirect to a detail view or another page.
    
    return render(request, 'edit_post.html', {"product": product, 'form': form, 'categories': categories})

def delete_post(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('home')
    

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
            
            messages.success(request, f'Hi {name} Your message has been sent successfully!')
            form = ContactForm()  # Reset the form
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def post_form(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'post_form.html',{'form':form, 'categories': categories})





