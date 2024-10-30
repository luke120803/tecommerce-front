from django_filters import rest_framework as filters

from teste import models
from teste.serializers import SaleSerializer

# Filtros de pesquisa
LIKE = 'unaccent__icontains'
ICONTAINS = 'icontains'
UNACCENT_IEXACT = 'unaccent__iexact'
EQUALS = 'exact'
STARTS_WITH = 'startswith'
GT = 'gt'
LT = 'lt'
GTE = 'gte'
LTE = 'lte'
IN = 'in'


class ClientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=ICONTAINS)
    cpf_sw = filters.CharFilter(field_name='cpf', lookup_expr=STARTS_WITH)
    rg = filters.CharFilter(lookup_expr=STARTS_WITH)
    age = filters.NumberFilter(lookup_expr=GT)

    class Meta:
        model = models.Client
        fields = ['name', 'cpf_sw', 'rg', 'age']


class ProductFilter(filters.FilterSet):
    quantity = filters.NumberFilter(lookup_expr=EQUALS)
    quantity_gt = filters.NumberFilter(field_name='quantity', lookup_expr=GT)
    description = filters.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Product
        fields = ['description', 'quantity', 'quantity_gt']


class EmployeeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr=ICONTAINS)
    registration = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Employee
        fields = ['name', 'registration']


class SaleFilter(filters.FilterSet):
    client = filters.CharFilter(field_name='client__name', lookup_expr=ICONTAINS)
    cpf_client = filters.CharFilter(field_name='client__cpf', lookup_expr=STARTS_WITH)
    product = filters.CharFilter(field_name='product__description', lookup_expr=ICONTAINS)
    employee = filters.CharFilter(field_name='employee__name', lookup_expr=ICONTAINS)
    registration_employee = filters.CharFilter(field_name='employee__registration', lookup_expr=EQUALS)
    nrf = filters.CharFilter(lookup_expr=EQUALS)

    class Meta:
        model = models.Sale
        fields = ['client', 'cpf_client','registration_employee', 'product', 'employee', 'nrf']