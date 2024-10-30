from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Product(ModelBase):
    description = models.CharField(
        db_column='tx_description',
        null=False
    )
    quantity = models.IntegerField(
        db_column='nb_quantity',
        null=False,
    )
    class Meta:
        managed = True
        db_table = 'product'

class Client(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=70
    )
    cpf = models.CharField(
        db_column='tx_cpf',
        null=False,
        max_length=12
    )
    rg = models.CharField(
        db_column='tx_rg',
        null=False,
        max_length=12
    )
    age = models.IntegerField(
        db_column='nb_age',
        null=False,
    )
    user = models.ForeignKey(
        'auth.User',
        db_column='id_user',
        on_delete=models.PROTECT,
        null=False
    )

    class Meta:
        managed = True
        db_table = 'client'

class Employee(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=70
    )
    registration = models.CharField(
        db_column='tx_registration',
        null=False,
        max_length=15
    )

    class Meta:
        managed = True
        db_table = 'employee'

class Sale(ModelBase):
    client = models.ForeignKey(
        Client,
        db_column='id_client',
        on_delete=models.PROTECT,
        null=False
    )
    employee = models.ForeignKey(
        Employee,
        db_column='id_employee',
        on_delete=models.PROTECT,
        null=False
    )
    product = models.ForeignKey(
        Product,
        db_column='id_product',
        on_delete=models.PROTECT,
        null=False
    )
    nrf = models.CharField(
        db_column='tx_nrf',
        null=False,
        max_length=20
    )

    class Meta:
        managed = True
        db_table = 'sale'