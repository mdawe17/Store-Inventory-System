from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ItemsForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def homePage(request):
    items = Items.objects.all()
    context = {'items' : items}
    return render(request, 'home.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'login.html', context)

def updateItems(request, pk):
    item = Items.objects.get(Items_ID=pk) #Items_ID will need to be changed to items_id or whatever is in your models.py file
    form = ItemsForm(instance=item)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {'form' : form}
    return render(request,'update_items.html', context)

def search(request):
    return render(request, 'storeinventorydb/search.html')

def search_results(request):
    searchName = request.GET['name']

    query_set_name_filtered = []
    query_set_name = Items.objects.all()

    for object in query_set_name:
        if (searchName in object.items_name):
            query_set_name_filtered.append(object)
    context = {
        'object_list' : query_set_name_filtered
    }

    return render(request, 'storeinventorydb/search_results.html', context)



def createItem(request):
    form = NewItem()
    if request.method == "POST":
        form = NewItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
            
    context = {'form' : form}
    return render(request, 'storeinventorydb/cni.html', context)


def deleteOrder(request, pk):
	item = Items.objects.get(items_id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('/home')

	context = {'item':item}
	return render(request, 'storeinventorydb/delete.html', context)
