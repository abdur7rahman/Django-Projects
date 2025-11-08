from django import forms
from .models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','email','body')
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter the Name"
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':"Enter the Email ID"
            }),
            'body': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':"Enter the Comments"
            })
        }