from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import NewUserForm


class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("login-user") #login-user
    template_name = "registration/signup.html"