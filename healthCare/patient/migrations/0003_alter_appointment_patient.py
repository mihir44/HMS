# Generated by Django 3.2.6 on 2021-10-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.CharField(default='', max_length=50),
        ),
    ]
