from django import forms

from tenis.models import tenis
    
class TenisForm(forms.ModelForm):
    class Meta:
        model = tenis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['photo'].required = False