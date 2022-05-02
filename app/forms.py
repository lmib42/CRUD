from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('memo','number','category','memo_ex')
        widgets = {
                    'memo': forms.TextInput(),
                    'number': forms.NumberInput(attrs={'min':1}),
                    'category': forms.RadioSelect(),
                    'memo_ex': forms.Textarea(attrs={'rows':4}),
                  }
