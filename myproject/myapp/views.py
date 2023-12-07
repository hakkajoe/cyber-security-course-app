from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'entry_list.html', {'entries': entries})

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'add_entry.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entry_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'entry_confirm_delete.html'
    success_url = reverse_lazy('entry_list')