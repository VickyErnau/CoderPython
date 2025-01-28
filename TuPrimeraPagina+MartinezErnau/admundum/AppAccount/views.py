from django.shortcuts import render, redirect
from .forms import User, UpdateUserForm, CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView


def error(request):
    return render(request, "error.html")

def modulo_admin():
    return redirect('admin')


def register_user(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"]
                                ,password=formulario.cleaned_data["password1"])
            login(request,user)
            data['form'] = formulario
            return render(request, "index.html")
        else:
            return redirect('error')
    return render(request, 'registration/register_user.html', data)

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            login(request, current_user)
            return redirect('profile_user')
        data = {
            'form': form
        }
        return render(request, 'registration/update_user.html', data)
    else:
        return redirect('error')

def logout_user(request):
    logout(request)
    return render(request, "index.html")

def password_changed(request):
    return render(request, "registration/password_changed.html")

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile_user.html'

    def get_object(self):
        return self.request.user

class PassChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_changed')