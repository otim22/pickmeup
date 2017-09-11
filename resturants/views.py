from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import ResturantCreateForm, ResturantLocationCreateForm
from .models import ResturantLocation

class ResturantListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return ResturantLocation.objects.filter(owner=self.request.user)

class ResturantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return ResturantLocation.objects.filter(owner=self.request.user)

class ResturantCreateView(LoginRequiredMixin, CreateView):
    form_class = ResturantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = '/resturants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ResturantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ResturantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Resturant'
        return context

class ResturantUpdateView(LoginRequiredMixin, CreateView):
    form_class = ResturantLocationCreateForm
    login_url = '/login/'
    template_name = 'resturants/detail.html'
    #success_url = '/resturants/'

    def get_context_data(self, *args, **kwargs):
        context = super(ResturantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Resturant: {name}'
        return context

    def get_queryset(self):
        return ResturantLocation.objects.filter(owner=self.request.user)
