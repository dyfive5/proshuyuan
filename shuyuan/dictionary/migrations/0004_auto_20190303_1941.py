# Generated by Django 2.1.7 on 2019-03-03 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20190303_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='id',
        ),
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dictionary.WordType'),
        ),
    ]
