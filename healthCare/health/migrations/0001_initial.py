# Generated by Django 2.2.14 on 2021-10-19 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default='', max_length=50)),
                ('issue', models.CharField(choices=[('Accident', 'Accident'), ('Stroke/Attack', 'Stroke/Attack'), ('Injury', 'Injury'), ('Others', 'Others')], default='', max_length=50)),
                ('email', models.CharField(default='', max_length=25)),
                ('phone', models.CharField(default='', max_length=10)),
                ('requirement', models.CharField(choices=[('ICU', 'ICU'), ('OXYGEN CYLINDER', 'OXYGEN CYLINDER'), ('VENTILATOR', 'VENTILATOR')], default='', max_length=50)),
                ('bloodgroup', models.CharField(default='', max_length=7)),
                ('address', models.CharField(default='', max_length=250)),
                ('medicine', models.CharField(default='', max_length=225)),
                ('allergy', models.CharField(default='', max_length=225)),
                ('hospitalsname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dname', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
