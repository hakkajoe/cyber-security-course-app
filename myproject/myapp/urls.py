# myproject/myapp/urls.py
from django.urls import path
from .views import entry_list, add_entry, register_view, EntryDeleteView

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('add_entry/', add_entry, name='add_entry'),
    path('register/', register_view, name='register'),
    path('delete_entry/<int:pk>/', EntryDeleteView.as_view(), name='delete_entry'),
]