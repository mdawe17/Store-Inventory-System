from django.forms import ModelForm
from .models import *


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['Items_ID', 'Items_Name', 'Items_Stock', 'Items_Sale_Price', 'Items_Department'] #These attribute names are different in your models.py file 
                                                                                                   #you will need to change them to 'items_id' for example
                                                                                                   
