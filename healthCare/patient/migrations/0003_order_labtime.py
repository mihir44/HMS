# Generated by Django 3.2.6 on 2021-10-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='labtime',
            field=models.CharField(choices=[('08:00 – 09:00', '08:00 – 09:00'), ('09:00 – 10:00', '09:00 – 10:00'), ('10:00 – 11:00', '10:00 – 11:00'), ('11:00 – 12:00', '11:00 – 12:00'), ('12:00 – 13:00', '12:00 – 13:00'), ('13:00 – 14:00', '13:00 – 14:00'), ('14:00 – 15:00', '14:00 – 15:00'), ('15:00 – 16:00', '15:00 – 16:00'), ('16:00 – 17:00', '16:00 – 17:00'), ('17:00 – 18:00', '17:00 – 18:00')], default='labtime', max_length=25),
        ),
    ]
