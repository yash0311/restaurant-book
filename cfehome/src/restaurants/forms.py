from django import forms

from .models import RestaurantLocation
from .validators import validate_category

class RestaurantLocationCreateForm(forms.ModelForm):
    
    category = forms.CharField(required=False)
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
            'slug',
        ]