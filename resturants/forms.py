from django import forms
from .models import ResturantLocation

class ResturantCreateForm(forms.Form):
    name      = forms.CharField()
    location  = forms.CharField(required=False)
    category  = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class ResturantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = ResturantLocation
        fields = [
            'name',
            'location',
            'category',
        ]
        
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name