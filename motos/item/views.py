from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

#Importamos "Q" esto hace que sea mas facil buscar en multiples campos
from django.db.models import Q
from .models import Category, Item
from .forms import EditItemForm, NewItemForm

# Create your views here.

def items(req):
    #Obtiene todos los articulos de la DB que se venden
    query = req.GET.get('query', '')
    category_id = req.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category_id=category_id)
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(req, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(req, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(req, 'item/detail.html', {
        'item' : item,
        'related_items': related_items
    })
    
@login_required
#Si desea intentar visitar esto (sin estar autenticado) sera redirigido a la pagina de inicio de sesion
def NewItem(req):
    if req.method == 'POST':
        form = NewItemForm(req.POST, req.FILES)      
        #1:25:41
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = req.user
            item.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm() #Instancia la class NewItemForm
    
    return render(req, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
#Si desea intentar visitar esto (sin estar autenticado) sera redirigido a la pagina de inicio de sesion
#Edita un item
def EditItem(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    if req.method == 'POST':
        form = EditItemForm(req.POST, req.FILES, instance=item)
        
        if form.is_valid():
            item.save()
            
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item) #Instancia la class NewItemForm
    
    return render(req, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })


#Funcion para eliminar un item
@login_required
def DeleteItem(req, pk):
    item = get_object_or_404(Item, pk=pk, created_by=req.user)
    item.delete()
    
    return redirect('dashboard:index')
