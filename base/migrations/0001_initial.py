# Generated by Django 5.0.2 on 2024-05-02 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=100)),
                ('property_type', models.CharField(max_length=100)),
                ('property_address', models.CharField(max_length=100)),
                ('property_size', models.IntegerField(default=0)),
                ('property_bedroom', models.IntegerField(default=0)),
                ('property_bathroom', models.IntegerField(default=0)),
                ('rent_amount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
