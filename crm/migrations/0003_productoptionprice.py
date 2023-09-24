# Generated by Django 4.2.2 on 2023-09-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_delete_productoptionprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOptionPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_price', models.IntegerField()),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.productoption')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.product')),
            ],
        ),
    ]
