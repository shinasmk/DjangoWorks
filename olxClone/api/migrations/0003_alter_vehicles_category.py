# Generated by Django 4.1.5 on 2023-03-15 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vehicles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.category'),
        ),
    ]
