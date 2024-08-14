from django.shortcuts import render, redirect
from .models import Inventory, RollerSkate
from .forms import InventoryForm, RollerSkateForm
from django.views import generic
from django.urls import reverse_lazy   

class HomeView(generic.TemplateView):
    template_name = 'RollerSkateInventory/home.html'    

#region InventoryViews
class InventoryListView(generic.ListView):
    model = Inventory
    context_object_name = 'inventories'

class InventoryCreateView(generic.CreateView):
    model = Inventory
    form_class = InventoryForm
    success_url = reverse_lazy('inventory-list')
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_name'] = "Create"            
        return context
    
class InventoryDetailView(generic.DetailView):    
    model = Inventory
    context_object_name = 'inventory'
    
class InventoryUpdateView(generic.UpdateView):    
    model = Inventory
    fields = ['name', 'address']
    success_url = reverse_lazy('inventory-list')    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_name'] = "Update"            
        return context
    
class InventoryDeleteView(generic.DeleteView):    
    model = Inventory
    success_url = reverse_lazy('inventory-list')
#endregion

class RollerSkateCreateView(generic.CreateView):
    model = RollerSkate
    form_class = RollerSkateForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventory_pk"] = self.kwargs['pk']
        context["button_name"] = "Create"
        return context    
    
    def form_valid(self, form):
        inventory_id = self.kwargs['pk']
        inventory = Inventory.objects.get(pk=inventory_id)
        form.instance.inventory = inventory
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.inventory.id})    

class RollerSkateDetailView(generic.DetailView):    
    model = RollerSkate
    context_object_name = 'rollerskate'

class RollerSkateUpdateView(generic.UpdateView):    
    model = RollerSkate
    fields = ['name', 'size_min', 'size_max', 'barcode']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['inventory_pk'] = self.kwargs['inventory_pk']
        context['button_name'] = "Update"            
        return context
    
    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.inventory.id})    

class RollerSkateDeleteView(generic.DeleteView):    
    model = RollerSkate
    
    def get_success_url(self):
        return reverse_lazy('inventory-detail', kwargs={'pk': self.object.inventory.id})       