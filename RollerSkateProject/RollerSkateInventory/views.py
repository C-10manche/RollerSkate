from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory, RollerSkate
from .forms import InventoryForm, RollerSkateForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory


def View_Home(request):
    template = 'RollerSkateInventory/home.html'
    return render(request, template)       

#region InventoryViews    
def List_Inventory(request):
    inventories = Inventory.objects.all()
    template = "RollerSkateInventory/inventory_list.html"
    context = {
            'inventories' : inventories,
            'cancel': reverse_lazy('home'),
               }
    return render(request, template, context)

def Create_Inventory(request):
    form = InventoryForm()
    template = "RollerSkateInventory/basic_form.html"
    url = reverse_lazy('inventory-list')
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url)
    context = {
            'form' : form, 
            'object' : "New Inventory",
            'button_name' : "Create", 
            'class' : "inventory", 
            'title' : "Creating",
            'cancel': url,
               }
    return render(request, template, context)

def Update_Inventory(request, pk):
    inventory = Inventory.objects.get(id=pk)
    form = InventoryForm(instance=inventory)
    template = "RollerSkateInventory/basic_form.html"
    url = reverse_lazy('inventory-list')
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect(url)
    context = {
            'form' : form,
            'object' : inventory.name,
            'button_name' : "Update", 
            'class' : "inventory", 
            'title' : f"Updating",
            'cancel': url,
            }
    return render(request, template, context)   

def Detail_Inventory(request, pk):    
    inventory = Inventory.objects.get(id=pk)
    template = 'RollerSkateInventory/inventory_detail.html'
    url = reverse_lazy('inventory-list') 
    rollerskate_number = 0
    
    for rollerskate in inventory.rollerskates.all():
        rollerskate_number += 1 
    
    context = {
            'inventory': inventory,
            'rollerskate_number': rollerskate_number,
            'cancel': url,
            }
    return render(request, template, context)

def Delete_Inventory(request, pk):  
    inventory = Inventory.objects.get(id=pk)
    url = reverse_lazy('inventory-list')
    template = "RollerSkateInventory/basic_confirm_delete.html"
    
    if request.method == 'POST':
        inventory.delete()
        return redirect(url)
    context = {
            'object': inventory,
            'class' : "inventory",
            }
    return render(request, template, context)   
#endregion

#region RollerSkateViews
def Create_RollerSkate(request, pk):
    inventory = Inventory.objects.get(id=pk)
    RollerSkateFormset = inlineformset_factory(Inventory, RollerSkate, 
                                               fields=("name", "size_min", "size_max", "barcode", "inventory"), 
                                               extra=1,
                                               can_order=False,
                                               can_delete=False,
                                               )
    url = reverse_lazy('inventory-detail', kwargs={'pk': inventory.pk})
    
    if request.method == 'POST':        
        formset = RollerSkateFormset(request.POST, instance=inventory)  
                  
        if formset.is_valid():
            formset.save()
            return redirect(url)
    else:
        formset = RollerSkateFormset(queryset=RollerSkate.objects.none(), instance=inventory)

    context = {
        'formset': formset,
        'object': "New Roller-Skate",
        'button_name': "Create",
        'class': "rollerskate",
        'title': "Creating",
        'cancel': url,
    }
    return render(request, "RollerSkateInventory/basic_formset.html", context)
    
def Update_Multiple_RollerSkate(request, inventory_pk):
    inventory = Inventory.objects.get(id=inventory_pk)
    RollerSkateFormset = inlineformset_factory(Inventory, RollerSkate, 
                                               fields=("name", "size_min", "size_max", "barcode", "inventory"), 
                                               extra=0,
                                               can_order=False,
                                               can_delete=False,
                                               )
    url = reverse_lazy('inventory-detail', kwargs={'pk': inventory_pk})
    
    if request.method == 'POST':        
        formset = RollerSkateFormset(request.POST, instance=inventory)                  
        if formset.is_valid():
            formset.save()
            return redirect(url)
    else:
        formset = RollerSkateFormset(queryset=RollerSkate.objects.all(), instance=inventory)

    context = {
        'formset': formset,
        'object': formset.instance.name,
        'button_name': "Update",
        'class': "rollerskate",
        'title': "Updating",
        'cancel': url,
    }
    return render(request, "RollerSkateInventory/basic_formset.html", context)
    

def Update_RollerSkate(request, pk, inventory_pk):
    rollerskate = RollerSkate.objects.get(id=pk)
    form = RollerSkateForm(instance=rollerskate)
    url = reverse_lazy('inventory-detail', kwargs={'pk': inventory_pk})
    template = "RollerSkateInventory/basic_form.html"
    
    if request.method == 'POST':
        form = RollerSkateForm(request.POST, instance=rollerskate)
        if form.is_valid():
            form.save()
            return redirect(url)
    context = {
            'form' : form, 
            'object' : form.instance.name,
            'button_name' : "Update", 
            'class' : "inventory", 
            'title' : "Updating",
            'cancel': url,
            }
    return render(request, template, context)

def Detail_RollerSkate(request, pk, inventory_pk):    
    rollerskate = RollerSkate.objects.get(id=pk)
    template = 'RollerSkateInventory/rollerskate_detail.html'
    url = reverse_lazy('inventory-detail', kwargs={'pk': inventory_pk}) 
    
    context = {
            'rollerskate': rollerskate,
            'class' : "rollerskate", 
            'cancel': url,
            }
    return render(request, template, context)
    
def Delete_RollerSkate(request, pk, inventory_pk):  
    rollerskate = RollerSkate.objects.get(id=pk)
    url = reverse_lazy('inventory-detail', kwargs={'pk': inventory_pk})
    template = "RollerSkateInventory/basic_confirm_delete.html"
    
    if request.method == 'POST':
        rollerskate.delete()
        return redirect(url)
    context = {
            'object': rollerskate,
            'class' : "rollerskate",
            }
    return render(request, template, context)
#endregion