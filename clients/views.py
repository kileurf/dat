from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientForm

def index(request):
    latest_clients_list = Client.objects.all()
    context = {'latest_clients_list': latest_clients_list}
    return render(request, 'clients/index.html', context)

@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('infras:create_infra'))
            return HttpResponseRedirect(reverse('clients:index'))
    else:
        form = ClientForm()

    return render(request, 'clients/client.html', {'form': form})

@login_required
def modify_client(request, slug):
    client = get_object_or_404(Client, slug=slug)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clients:index'))
    else:
        form = ClientForm(instance=client)

    return render(request, 'clients/client.html', {'form': form})

@login_required
def delete_client(request, slug):
    client = get_object_or_404(Client, slug=slug).delete()

    return HttpResponseRedirect(reverse('clients:index'))
