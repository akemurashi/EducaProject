# Generated by Django 3.2.8 on 2021-12-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_apuntes'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuntes',
            name='ramo_apunte',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.ramos_usuario'),
        ),
    ]
