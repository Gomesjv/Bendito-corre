from tenis.forms import TenisForm
from tenis.models import tenis
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class TenisListView(ListView):
    model = tenis 
    template_name = 'tenis.html'
    context_object_name = 'tenis' 

    def get_queryset(self):
        tenis_query = super().get_queryset().order_by('name')   # <-- usar 'name' (campo real)
        search = self.request.GET.get('search')
        if search:
            tenis_query = tenis_query.filter(name__icontains=search)  # <-- usar 'name__icontains'
        return tenis_query

class TenisDetailView(DetailView):
    model = tenis
    template_name = 'tenis_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch') 
class NewTenisView(CreateView):
    model = tenis
    form_class = TenisForm
    template_name = 'new_tenis.html'
    success_url = '/tenis/'   
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class TenisUpdateView(UpdateView):
    model = tenis
    form_class = TenisForm
    template_name = 'tenis_update.html'

    def get_success_url(self):
        return reverse_lazy('tenis_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch') 
class DeleteTenisView(DeleteView):
    model = tenis
    template_name = 'tenis_delete.html'
    success_url = '/tenis/'