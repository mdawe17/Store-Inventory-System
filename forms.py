from django.forms import ModelForm
from .models import *


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['Items_ID', 'Items_Name', 'Items_Stock', 'Items_Sale_Price', 'Items_Department']
