from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View,UpdateView,DetailView
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from edu.utils import password_reset_token
from .models import *
from .forms import *

class ObourMixin(): 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Student.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/student-login/')
        return super().dispatch(request, *args, **kwargs)

class HomeView(ObourMixin,CreateView):
    template_name = 'home.html' 
    form_class = WhoGetOfferForm
    success_url = '?m=get_offer'
    
    def form_valid(self, form):
        full_name = form.cleaned_data.get('full_name')
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        return super(HomeView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student']   = Student.objects.get(user=self.request.user)
        context['wgoff']   = WhoGetOffer.objects.latest('-id')
        context['all_courses'] = Course.objects.all().order_by('-id')
        context['off'] = Offer.objects.latest('-id')
        context['g_images'] = Galary.objects.all().order_by('-id')
        return context
    
class StudentRegisterView(CreateView):
    template_name='student_register.html'
    form_class = StudentRegisterForm
    success_url = '/'
    def form_valid(self, form):
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username,email,password)
            form.instance.user = user
            login(self.request,user)
            return super().form_valid(form)

class StudentLoginView(FormView):
    template_name = 'student_login.html'
    form_class = StudentLoginForm
    success_url = '/'
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request,username=username,password=password)
        if user is not None and Student.objects.filter(user=user).exists():
            login(self.request,user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)  

class StudentLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class StudentProfileView(TemplateView):
    template_name = 'student_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student']   = Student.objects.get(user=self.request.user)
        context['available_languages'] = ['en','ar']
        return context

class UpdateProfileView(UpdateView):
    model = Student
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'

    def get_object(self,*args,**kwargs):
        client = get_object_or_404(Student, pk=self.kwargs['id'])
        return client

    def get_success_url(self):
        success_url = reverse_lazy('edu:profile')
        return success_url
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_languages'] = ['en','ar']
        return context

class ForgotPasswordView(FormView):
    template_name = 'forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = '/forget-password/?m=s'
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        url = self.request.META['HTTP_HOST']
        client = Student.objects.get(user__email=email)
        user = client.user
        text_content = f'Dear Student , {client.full_name} ! You have requested a password reset for your account at {email}. Please go to the following page and add a new password.\n'
        html_content = "http://"+ url + "/reset-password/" + email+ "/" +password_reset_token.make_token(user)+"/"
        send_mail(
            'Password Reset Link | Obour Institute',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)
    
class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
    form_class = PasswordResetForm
    success_url = '/student-login/'
    def form_valid(self, form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get('email')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)
