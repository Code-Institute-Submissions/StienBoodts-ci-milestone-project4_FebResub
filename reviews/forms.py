from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = Product.objects.all()
        name = [(c.id, c.name) for c in products]

        self.fields['product'].choices = name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
