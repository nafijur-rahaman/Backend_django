from django.http import HttpResponse
from django.shortcuts import render,redirect
from author.forms import RegisterForm,userChangeData
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

def register(request):
    if request.method=='POST':
        
        author_form=RegisterForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            messages.success(request,'Account create Successfully')
            return redirect("register")
    else:
        author_form=RegisterForm()
    return render(request,"register.html",{'form':author_form,'type':'Register'})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Log in Successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Enter valid information')
                return redirect('register')
    else:
        form=AuthenticationForm()
    return render(request,'./register.html',{'form':form,'type':'Login'})



class UserLogin(LoginView):
    template_name='register.html'
    def get_success_url(self):
   
        return reverse_lazy('profile')
    
    
    def form_valid(self, form):
        messages.success(self.request,'Log in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,"Enter valid information")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='login'
        return context
    
@method_decorator(login_required,name='dispatch')
class UserLogout(LogoutView):
    next_page = reverse_lazy('homepage')
    

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})

@login_required
def edit_profile(request):
    if request.method=="POST":
        form=userChangeData(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile update successfully")
            return redirect('profile')
    else:
        form=userChangeData(instance=request.user)
    return render(request,'edit_profile.html',{'form':form})

def pass_change(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password update successfully")
            update_session_auth_hash(request,form.user)
            return redirect("profile")
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



