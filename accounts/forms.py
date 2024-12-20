from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Enter your username',
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Enter your email',
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'id': 'id_password1',
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 pr-10 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Enter your password',
        })
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
            'id': 'id_password2',
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 pr-10 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Confirm your password',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            print(f"Email {email} already exists!") 
            raise forms.ValidationError('Email already registered. Please use a different email.')
        return email

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Enter your email or username',
            'id': 'id_username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 pr-10 focus:outline-none focus:ring-[#54C2F0] focus:border-[#54C2F0] text-sm dark:bg-[#14171A] dark:text-white',
            'placeholder': 'Enter your password',
            'id': 'id_password',
        })
    )

    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        # Cek apakah input adalah email
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username_or_email = user.username  # Ganti input dengan username yang sesuai
            except User.DoesNotExist:
                raise forms.ValidationError("User with this email does not exist.")
        
        # Gunakan input yang sudah disesuaikan untuk autentikasi
        self.cleaned_data['username'] = username_or_email
        return super(UserLoginForm, self).clean()