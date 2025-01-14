
from django import forms
from . import models
from django import forms
from django.utils.timezone import now
from .models import Product, Category

class ContactForm(forms.Form):
	name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),required = True)
	customer_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required = True)
	message = forms.CharField(label="", max_length=500, widget=forms.Textarea(attrs={
		'class':'form-control', 
		'placeholder':'Message here',
		'rows': 5,
		}),
		required = True)

	class Meta:
		fields = ('name','customer_email','message')


class ContactForm(forms.Form):
	name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),required = True)
	customer_email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required = True)
	message = forms.CharField(label="", max_length=500, widget=forms.Textarea(attrs={
		'class':'form-control', 
		'placeholder':'Message here',
		'rows': 5,
		}),
		required = True)

	class Meta:
		fields = ('name','customer_email','message')


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'required': True})
    )
    subtitle = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'subtitle', 'placeholder': 'Optional'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'category', 'required': True})
    )
    image = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image', 'accept': 'image/*'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': 4, 'placeholder': 'Optional'})
    )
    image_one = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image_one', 'accept': 'image/*'})
    )
    description_one = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description_one', 'rows': 2, 'placeholder': 'Optional'})
    )
    image_two = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image_two', 'accept': 'image/*'})
    )
    description_two = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description_two', 'rows': 2, 'placeholder': 'Optional'})
    )
    video_url = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'class': 'form-control', 'id': 'video_url', 'placeholder': 'Optional'})
    )
    video_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'video_description', 'rows': 2, 'placeholder': 'Optional'})
    )

    class Meta:
        model = Product
        fields = [
            'title', 'subtitle', 'category', 'image', 'description',
            'image_one', 'description_one', 'image_two', 'description_two',
            'video_url', 'video_description'
        ]

		