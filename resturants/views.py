from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import ResturantCreateForm, ResturantLocationCreateForm
from .models import ResturantLocation

def resturant_createview(request):
    form = ResturantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/resturants/")
    if form.errors:
        errors = form.errors

    template_name = 'resturants/form.html'
    context = {
        "form": form, 
        "errors": errors
    }
    return render(request, template_name, context)

def resturant_listview(request):
    template_name = 'resturants/resturants_list.html'
    queryset = ResturantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class ResturantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = ResturantLocation.objects.filter(
                        Q(category__iexact=slug) |
                        Q(category__icontains=slug) 
                    )
        else:
            queryset = ResturantLocation.objects.all()
        return queryset

class ResturantDetailView(DetailView):
    queryset = ResturantLocation.objects.all()

class ResturantCreateView(CreateView):
    form_class = ResturantLocationCreateForm
    template_name = 'resturants/form.html'
    success_url = '/resturants/'
