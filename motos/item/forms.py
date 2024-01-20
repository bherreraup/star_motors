from django import forms
from .models import Item


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

#Crea un item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        #Minute Video 1:16:47
        fields = ('category', 'name', 'description', 'image', 'price', 'is_sold')
        widgets = {
            'category': forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            })
        }

#Edita un item
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        #Minute Video 1:37:20
        fields = ('name', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class' : INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            })
        }