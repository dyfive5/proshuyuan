# Generated by Django 2.1.7 on 2019-03-03 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20190303_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='dictionary.WordType'),
        ),
    ]