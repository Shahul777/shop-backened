from django.db import models

# Create your models here.
class AccountExpenses(models.Model):
   

    Date = models.DateField()
    DateString =models.CharField(max_length=20)
    MonthString =models.CharField(max_length=20)
    YearString =models.CharField(max_length=20)
    Grocerry = models.IntegerField()
    Entertainment=models.IntegerField()
    Maintanence = models.IntegerField()
    ShopCurrentBill = models.IntegerField()
    HomeCurrentBill =models.IntegerField()
    PaperCost = models.IntegerField()
    BlackTonerCost = models.IntegerField()
    ColourTonerCost = models.IntegerField()
    Bindings = models.IntegerField(default=0)
    Others = models.IntegerField(default=0)
    BlackMachineMaintanence = models.IntegerField()
    ColourMachineMaintanence = models.IntegerField()
    MoneyDeposit = models.IntegerField()
    PaytmExpense = models.IntegerField()
    CashExpense =  models.IntegerField()
    TotalExpense =  models.IntegerField()
    TotalProfit =  models.IntegerField()


class RateSheet(models.Model):
    ShahulSalary = models.DecimalField(default=1466.66,max_digits=9 , decimal_places=2)
    VeperyIncome = models.DecimalField(default=1266.66 ,max_digits=9 , decimal_places=2 )
    VaadagaiIncome=  models.DecimalField(default=233.33 ,max_digits=9 , decimal_places=2 )
    CurrentBill = models.DecimalField(default=83.33,max_digits=9 , decimal_places=2)
    HomeLoan = models.DecimalField(default=1066.66,max_digits=9 , decimal_places=2)

