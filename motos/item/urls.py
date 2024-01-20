from django.urls import path
from . import views as vw_itm

app_name = 'item'

urlpatterns = [
    path('', vw_itm.items, name='items'),
    path('new/', vw_itm.NewItem, name='new_item'),
    path('<int:pk>/', vw_itm.detail, name='detail'),
    path('<int:pk>/delete/', vw_itm.DeleteItem, name='delete'),
    path('<int:pk>/edit/', vw_itm.EditItem, name='edit'),
]
