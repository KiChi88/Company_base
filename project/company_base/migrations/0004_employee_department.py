# Generated by Django 2.0.7 on 2018-12-01 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company_base', '0003_auto_20181201_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company_base.Department', verbose_name='Отдел'),
        ),
    ]