# Generated by Django 4.0.3 on 2024-04-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsmsApp', '0007_laundry_address_alter_laundry_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]