# Generated by Django 3.2.16 on 2023-03-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopAccountKdm', '0002_alter_accountexpenses_gettime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombinedEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('TotalIncome', models.IntegerField()),
                ('NetProfit', models.IntegerField()),
                ('TotalExpense', models.IntegerField()),
                ('BlackReading', models.IntegerField()),
                ('ColourReading', models.IntegerField()),
                ('PaperUsed', models.IntegerField()),
                ('PaperCost', models.IntegerField()),
                ('Rent', models.IntegerField()),
                ('CurrentBill', models.IntegerField()),
                ('LabourSalary', models.IntegerField()),
                ('ExpenseCalculated', models.IntegerField()),
                ('isExecuted', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyEntryKdm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Month', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('TotalIncome', models.IntegerField()),
                ('NetProfit', models.IntegerField()),
                ('TotalExpense', models.IntegerField()),
                ('BlackReading', models.IntegerField()),
                ('ColourReading', models.IntegerField()),
                ('TajPresent', models.IntegerField()),
                ('NoorPresent', models.IntegerField()),
                ('LabourSalary', models.IntegerField()),
                ('Rent', models.IntegerField()),
                ('CurrentBill', models.IntegerField()),
                ('Expenses', models.IntegerField()),
                ('ExpenseCalculated', models.IntegerField()),
                ('ExpensePercentCalculate', models.IntegerField()),
                ('PaperDay1', models.IntegerField()),
                ('PaperLast', models.IntegerField()),
                ('PaperArrivedTotal', models.IntegerField()),
                ('PaperUsed', models.IntegerField()),
                ('PaperCost', models.IntegerField()),
                ('isExecuted', models.IntegerField()),
            ],
        ),
    ]
