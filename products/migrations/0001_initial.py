# Generated by Django 5.0.1 on 2024-05-14 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='brands.brand')),
                ('categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categorie', to='categories.categorie')),
            ],
        ),
    ]
