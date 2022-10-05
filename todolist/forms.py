from todolist.models import Task
from django import forms
class todolist_form(forms.ModelForm):
    class Meta:
        model = Task
        fields =('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan judul'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan deskripsi'}),
        }