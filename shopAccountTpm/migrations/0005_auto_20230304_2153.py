# Generated by Django 3.2.16 on 2023-03-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountTpm', '0004_alter_monthlyentrytpm_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyentrytpm',
            name='AssanPresent',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='monthlyentrytpm',
            name='ManiPresent',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='monthlyentrytpm',
            name='RasheedPresent',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=9),
        ),
    ]
