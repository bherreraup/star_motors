from django.shortcuts import redirect, render
# Create your views here.

from item.models import Category, Item
from .forms import SingupForm

#Items Views
def index(req):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(req, 'motors/index.html', {
        'categories' : categories,
        'items' : items,
    })

#Contact Views
def contact(req):
    return render(req, 'motors/contact.html')

#Form Sing Up Views
def singup(req):
    
    if req.method == 'POST':
        form = SingupForm(req.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SingupForm
    
    return render(req, 'motors/singup.html', {
        'form' : form
    })