from django import forms
from .models import GoogleForm

class GoogleFormForm(forms.ModelForm):
    class Meta:
         model = GoogleForm
         fields = ['form_id','title','description']
         widgets = {
             'form_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter form_id name'}),
             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title Number'}),
             'description': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter  description'}),
            
}
