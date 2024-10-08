from django.shortcuts import render, redirect
from .models import Event, Order
from .forms import EventForm
from django.urls import reverse_lazy

# Create your views here.
def List_Event(request):
    template = "Event/event_list.html"
    events = Event.objects.all()
    context ={
        'events': events,
    }
    return render(request, template, context)

def Create_Event(request):
    form = EventForm()
    template = "Inventory/basic_form.html"
    url = reverse_lazy('event-list')
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url)
    context = {
            'form' : form, 
            'object' : "New Event",
            'button_name' : "Create", 
            'class' : "event", 
            'title' : "Creating",
            'cancel' : url,
            }
    return render(request, template, context)

def Update_Event(request, pk):
    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)
    template = "Inventory/basic_form.html"
    url = reverse_lazy('event-list')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect(url)
    context = {
            'form' : form,
            'object' : event.name,
            'button_name' : "Update", 
            'class' : "event", 
            'title' : f"Updating",
            'cancel' : url,
            }
    return render(request, template, context)   

def Detail_Event(request, pk):    
    event = Event.objects.get(id=pk)
    template = 'Event/event_detail.html'
    url = reverse_lazy('event-list', kwargs={'pk': pk}) 
    
    context = {
            'event': event,
            'cancel': url,
            }
    return render(request, template, context)

def Delete_Event(request, pk):  
    event = Event.objects.get(id=pk)
    url = reverse_lazy('event-list')
    template = "Inventory/basic_confirm_delete.html"
    
    if request.method == 'POST':
        event.delete()
        return redirect(url)
    context = {
            'object': event,
            'class' : "event",
            }
    return render(request, template, context)   
