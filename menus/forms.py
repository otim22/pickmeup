from django import forms

from resturants.models import ResturantLocation

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'resturant',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        #print(kwargs.pop('instance'))
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['resturant'].queryset = ResturantLocation.objects.filter(owner=user) #.exclude(item__isnull=False)