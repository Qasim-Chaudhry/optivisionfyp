from django import forms
from .models import Contact
from .models import Blog
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'name', 'message']
        widgets = {
        'email': forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'form-control'}),
        'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control'}),
   
    }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Your Content', 'class': 'form-control'}),
        }