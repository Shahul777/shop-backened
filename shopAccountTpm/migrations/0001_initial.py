# Generated by Django 4.1.1 on 2022-10-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Day', models.CharField(max_length=20)),
                ('isSunday', models.IntegerField()),
                ('isHoliday', models.IntegerField()),
                ('isPaperCame', models.IntegerField()),
                ('PaperQuantityCame', models.IntegerField()),
                ('isPaperSent', models.IntegerField()),
                ('PaperQuantitySent', models.IntegerField()),
                ('isTonerCame', models.IntegerField()),
                ('isTonerSent', models.IntegerField()),
                ('TonerQuantityCame', models.IntegerField()),
                ('TonerQuantitySent', models.IntegerField()),
                ('isItemsCame', models.IntegerField()),
                ('ItemsInfo', models.CharField(max_length=200)),
                ('BlackMachineReading1', models.IntegerField()),
                ('BlackMachineReading2', models.IntegerField()),
                ('ColourMachineReading1', models.IntegerField()),
                ('ColourMachineReading2', models.IntegerField()),
                ('BlackCopies', models.IntegerField()),
                ('ColourCopies', models.IntegerField()),
                ('B2bCopies', models.IntegerField()),
                ('PaperPresentToday', models.IntegerField()),
                ('PaperSoldToday', models.IntegerField()),
                ('PaperSheet', models.IntegerField()),
                ('Toner', models.IntegerField()),
                ('TonerSpent', models.IntegerField()),
                ('Bindings', models.IntegerField()),
                ('Expenses', models.IntegerField()),
                ('TodayStayDetail', models.CharField(max_length=200)),
                ('PastStayDetail', models.CharField(max_length=200)),
                ('PastSoldDetail', models.CharField(max_length=200)),
                ('TodayStayingCopies', models.IntegerField()),
                ('TodayStayingMoney', models.IntegerField()),
                ('OldStayingMoney', models.IntegerField()),
                ('OldStayingCopies', models.IntegerField()),
                ('GoneCopiesPast', models.IntegerField()),
                ('GoneMoneyPast', models.IntegerField()),
                ('NotesToday', models.CharField(max_length=200)),
                ('CashIncome', models.IntegerField()),
                ('PaytmIncome', models.IntegerField()),
                ('TotalIncome', models.IntegerField()),
                ('OpeningBalance', models.IntegerField()),
                ('NetProfit', models.IntegerField()),
                ('GetTime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LabourExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Day', models.CharField(max_length=10)),
                ('GetTime', models.IntegerField()),
                ('AssanPresent', models.IntegerField()),
                ('AssanExpense', models.IntegerField()),
                ('RasheedPresent', models.IntegerField()),
                ('RasheedExpense', models.IntegerField()),
                ('ManiPresent', models.IntegerField()),
                ('ManiExpense', models.IntegerField()),
                ('isRasheedHalfDay', models.IntegerField()),
                ('isAssanHalfDay', models.IntegerField()),
                ('isManiHalfDay', models.IntegerField()),
            ],
        ),
    ]
