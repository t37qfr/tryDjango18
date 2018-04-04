from django import forms

from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=120,required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=300)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','full_name']

    '''CLEAN_FIELDNAME function name!!!'''
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base,provider = email.split('@')
        domain,extension = provider.split('.')
        if 'gmail' != domain:
            raise forms.ValidationError('Please use a Gmail address')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name