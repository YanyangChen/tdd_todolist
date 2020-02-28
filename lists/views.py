from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.http import *
from lists.forms import ItemForm
from lists.models import Item, List
# Create your views here.

# def home_page(request):
#     if request.method == 'POST':
#         Item.objects.create(text=request.POST['text'])
#         try:
#             item.full_clean()
#         except ValidationError:
#             error = "You can't have an empty list item"
#             return render(request, 'home.html', {"error": error})
#         return redirect('/lists/the-only-list-in-the-world/')
#     return render(request, 'home.html')

def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})

    return redirect(list_)

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    item=Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
    except ValidationError:
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        #Item.objects.create(text=request.POST['text'], list=list_)
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})