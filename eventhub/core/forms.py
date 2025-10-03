from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, Evenement


class EventForm(forms.ModelForm):
    class Meta:
        model = Evenement
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


from django import forms
from .models import Review

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    note = forms.IntegerField(
        label="Note (0/5)",
        min_value=0,
        max_value=5,
        initial=0,  # valeur par défaut 0
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0/5'
        })
    )

    commentaire = forms.CharField(
        label="Commentaire",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=True
    )

    image = forms.ImageField(
        label="Ajouter une image (optionnel)",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Review
        fields = ['note', 'commentaire', 'image']


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # On cache le help_text des champs de mot de passe
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # Ajouter classe bootstrap directement
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'