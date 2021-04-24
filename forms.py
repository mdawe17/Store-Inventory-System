from django.forms import ModelForm
from .models import *



class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['items_id', 'items_name', 'items_stock', 'items_sale_price', 'items_dept'] 
        #These attribute names are different in your models.py file 
        #you will need to change them to 'items_id' for example   


class NewItem(ModelForm): 
    class Meta:
        model = Items
        fields = "__all__"  
