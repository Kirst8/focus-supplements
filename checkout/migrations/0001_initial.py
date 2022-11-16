# Generated by Django 3.1.7 on 2021-03-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=20)),
                ('street_address_1', models.CharField(max_length=80)),
                ('street_address_2', models.CharField(max_length=80)),
                ('county', models.CharField(max_length=50)),
                ('eircode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('home_delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
            ],
        ),
    ]
