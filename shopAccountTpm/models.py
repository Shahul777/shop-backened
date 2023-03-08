from ssl import Options
from django.db import models

# Create your models here.
class AccountExpenses(models.Model):
    
    Date = models.DateField()
    Day =models.CharField(max_length=20)
    isSunday = models.IntegerField()
    isHoliday = models.IntegerField()
    isPaperCame= models.IntegerField()
    PaperQuantityCame = models.IntegerField()
    isPaperSent= models.IntegerField()
    
    PaperQuantitySent= models.IntegerField()
    isTonerCame= models.IntegerField()
    isTonerSent = models.IntegerField()
    TonerQuantityCame = models.IntegerField()
    TonerQuantitySent= models.IntegerField()
    isItemsCame =models.IntegerField()
    ItemsInfo = models.CharField(max_length=200)


    BlackMachineReading1 = models.IntegerField()
    BlackMachineReading2 = models.IntegerField()
    ColourMachineReading1= models.IntegerField()
    ColourMachineReading2= models.IntegerField()
    BlackCopies = models.IntegerField()
    ColourCopies = models.IntegerField()
    B2bCopies = models.IntegerField()
    PaperPresentToday = models.IntegerField()
    # PaperYesterday = models.DecimalField(max_digits=9 , decimal_places=3)
    PaperSoldToday =models.IntegerField()
    PaperSheet = models.IntegerField()
    Toner  = models.IntegerField()
    TonerSpent= models.IntegerField()
    Bindings = models.IntegerField()
    Expenses = models.IntegerField()
    TodayStayDetail = models.CharField(max_length=200)
    PastStayDetail= models.CharField(max_length=200)
    PastSoldDetail = models.CharField(max_length=200)
    TodayStayingCopies= models.IntegerField()
    TodayStayingMoney= models.IntegerField()
    OldStayingMoney =models.IntegerField()
    OldStayingCopies=models.IntegerField()
    GoneCopiesPast= models.IntegerField()
    GoneMoneyPast= models.IntegerField()
    NotesToday= models.CharField(max_length=200)
    CashIncome= models.IntegerField()
    PaytmIncome= models.IntegerField()
    TotalIncome = models.IntegerField()
    OpeningBalance = models.IntegerField()
    NetProfit= models.IntegerField()
    GetTime=models.BigIntegerField()

class LabourExpenses(models.Model):
    
    Date = models.DateField()
    Day =models.CharField(max_length=10)
    GetTime=models.BigIntegerField()
    AssanPresent = models.IntegerField()
    AssanExpense = models.IntegerField()
    RasheedPresent = models.IntegerField()
    RasheedExpense = models.IntegerField()
    ManiPresent = models.IntegerField()
    ManiExpense = models.IntegerField()
    isRasheedHalfDay =models.IntegerField()
    isAssanHalfDay=models.IntegerField()
    isManiHalfDay=models.IntegerField()
class MonthlyEntryTpm(models.Model):
    Month = models.CharField(max_length=200)
    Year = models.IntegerField()
    TotalIncome = models.IntegerField()
    NetProfit = models.IntegerField()
    TotalExpense = models.IntegerField()
    BlackReading = models.IntegerField()
    ColourReading = models.IntegerField()
    
    AssanPresent = models.DecimalField(default=0,max_digits=9 , decimal_places=1)
    ManiPresent = models.DecimalField(default=0,max_digits=9 , decimal_places=1)
    RasheedPresent = models.DecimalField(default=0,max_digits=9 , decimal_places=1)
    
    
    LabourSalary = models.IntegerField()
    Rent = models.IntegerField()
    CurrentBill = models.IntegerField()
    Expenses = models.IntegerField()
    ExpenseCalculated = models.IntegerField()
    ExpensePercentCalculate =  models.IntegerField()

    
    PaperDay1 = models.IntegerField()
    PaperLast = models.IntegerField()
    PaperArrivedTotal = models.IntegerField()
    PaperUsed = models.IntegerField()
    PaperCost = models.IntegerField()
    PaperSent = models.IntegerField(default=0)
    isEdited = models.IntegerField()

    isExecuted = models.IntegerField()