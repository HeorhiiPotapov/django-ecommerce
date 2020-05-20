import django_filters
from .models import Product
from django import forms


COLOR_CHOICES = (
    ('White', 'White'),
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Green', 'Green')
)


SIZE_CHOICES = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL')
)


TYPE_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class ProductFilter(django_filters.FilterSet):

    type = django_filters.MultipleChoiceFilter(
        choices=TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    color = django_filters.MultipleChoiceFilter(
        choices=COLOR_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    size = django_filters.MultipleChoiceFilter(
        choices=SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ('type', 'color', 'size')
