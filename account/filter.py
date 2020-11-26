import django_filters
from .models import *
from django_filters import DateFilter

# class OrderFilter(django_filters.FilterSet):
    
#     startDate = DateFilter(field_name='date_created', lookup_expr='gte')
#     class Meta:
#         model = Order
#         fields = '__all__'


