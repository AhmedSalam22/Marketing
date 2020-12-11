from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
from django.views.generic import CreateView
from .models import Info
# Create your views here.

class InfoView(CreateView):
    model = Info
    template_name = 'home/landing_page.html'
    success_url = reverse_lazy("home:home")

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "registration/register.html", {"form":form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account has been created successfully you can now log in')
            return redirect(reverse_lazy("home:home"))
        return render(request, "registration/register.html", {"form":form})

