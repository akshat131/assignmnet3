
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Tool
from .forms import UserForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class IndexView(generic.ListView):
    template_name = 'inventory/index.html'

    context_object_name = 'all_tools'
    def get_queryset(self):
        return Tool.objects.all()

class ToolCreate(CreateView):
    model = Tool
    fields = ['name', 'description', 'availability', 'price']

class ToolUpdate(UpdateView):
    model = Tool
    fields = ['name', 'description', 'availability', 'price']

class ToolDelete(DeleteView):
    model = Tool
    success_url = reverse_lazy('inventory:index')

def register(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('inventory:index')
        context = {
            "form": form,
        }
        return render(request, 'inventory/registration_form.html', context)


def logoutP(request):
    logout(request)

    return redirect('inventory:login')

def loginP(request):
    if request.user.is_authenticated:
        return redirect('inventory:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inventory:index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'inventory/login.html', context)