# myapp/forms.py
from django import forms
from .models import Item, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'unit', 'price']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select or leave blank'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Select an existing category.")

        return cleaned_data