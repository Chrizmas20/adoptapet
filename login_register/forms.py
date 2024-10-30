#changed
from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User  # Replace with your custom model if you're not using the default User model
        fields = ['first_name', 'last_name', 'age', 'contact_no', 'address', 'email', 'password']  # Define the fields

    # Optionally, add validation for confirm password
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

        return cleaned_data