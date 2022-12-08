from django import forms
from edu.models import *
from django.contrib.auth.models import User

class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
            model = Student
            fields = ['username','full_name','email','password']
    
    def clean_username(self):
            user_name = self.cleaned_data['username'] 
            qs = User.objects.filter(username=user_name)
            if qs.exists():
                raise forms.ValidationError("Student with this username already exists.")
            return user_name

class StudentLoginForm(forms.Form):
      username = forms.CharField(widget=forms.TextInput())
      password = forms.CharField(widget=forms.PasswordInput())
      def clean_username(self):
            user_name = self.cleaned_data['username'] 
            qs = User.objects.filter(username=user_name)
            if not qs.exists():
                  raise forms.ValidationError("Student with this username does not exist.")
            return user_name

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name','image','phone_number',
                  'objective','privacy','city','study_at','module']

class ForgotPasswordForm(forms.Form):
      email = forms.CharField(widget=forms.EmailInput(
            attrs={'class':"form-control",
            'placeholder':"Enter your email here .."}
      ))
      def clean_email(self):
            email = self.cleaned_data.get('email')
            qs = Student.objects.filter(user__email=email)
            if not qs.exists():
                  raise forms.ValidationError("Email does not exist.")
            return email

class PasswordResetForm(forms.Form):
      new_password = forms.CharField(widget=forms.PasswordInput(
            attrs={'class':"form-control",
            'autocomplete':"new-password",
            'placeholder':"Enter your Password here .."}
      ),label="New Password")

      confirm_password = forms.CharField(widget=forms.PasswordInput( 
            attrs={'class':"form-control",
            'autocomplete':"confirm-password",
            'placeholder':"Confirm your Password here .."}
      ),label="Confirm New Password")

      def clean_confirm_new_password(self):
            new_password = self.cleaned_data.get('new_password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if new_password != confirm_password:
                  raise forms.ValidationError("Password does not match.")
            return confirm_password
      
class WhoGetOfferForm(forms.ModelForm):
      class Meta:
            model = WhoGetOffer
            fields = ['full_name','email','phone']    
