# Generated by Django 4.2.2 on 2023-07-09 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('category_image', models.ImageField(blank=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('telegram_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('birthday', models.DateField(null=True)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField()),
                ('product_description', models.CharField(blank=True, max_length=500)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('Drinks', models.CharField(blank=True, choices=[('Sprite', 'Sprite'), ('Coca-Cola', 'Coca-Cola'), ('Fanta', 'Fanta')], max_length=9, null=True)),
                ('Snacks', models.CharField(blank=True, choices=[('Potato Balls', 'Potato Balls'), ('French Fries', 'French Fries'), ('Country Style Potato', 'Country Style Potato')], max_length=20, null=True)),
                ('Kids', models.CharField(blank=True, choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=7, null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.categorymodel')),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='crm.categorymodel', to_field='category_name')),
            ],
            options={
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_items', models.TextField()),
                ('payment_method', models.CharField(max_length=10)),
                ('order_address', models.CharField(blank=True, max_length=250, null=True)),
                ('order_comment', models.CharField(blank=True, max_length=500, null=True)),
                ('order_sum', models.IntegerField()),
                ('order_status', models.CharField(max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customermodel', to_field='telegram_id')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_coordinates', models.JSONField(blank=True, max_length=200, null=True)),
                ('address_text', models.CharField(blank=True, max_length=250, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customermodel', to_field='telegram_id')),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Createad On')),
                ('comment', models.TextField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customermodel', to_field='telegram_id')),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField()),
                ('product_options', models.JSONField(max_length=200, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customermodel', to_field='telegram_id')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.productmodel')),
            ],
        ),
    ]
