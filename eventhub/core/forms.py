from django import forms
from .models import Event, Review

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['titre', 'description', 'categorie', 'date', 'lieu', 'capacite', 'image']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categorie': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text', 'image']