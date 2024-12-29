from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    # metodo para validar si email esta registrado
    def clean_email(self):
        email = self.cleaned_data.get('email')  # obtenemos el campo email
        if User.objects.filter(email=email).exists():   # si el email existe en la tabla User
            raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser válido')

    class Meta:
        model = User
        fields = ['email']
    
    # metodo para validar si email esta registrado
    def clean_email(self):
        email = self.cleaned_data.get('email')  # obtenemos el campo email
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():   # si el email existe en la tabla User
                raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mt-3'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control mt-3', 
                'rows':3,
                'placeholder': 'Biografía'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Enlace'

            })
        }

        