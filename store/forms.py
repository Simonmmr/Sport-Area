
from django import forms

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
		