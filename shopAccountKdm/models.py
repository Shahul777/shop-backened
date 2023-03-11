from django.db import models

# Create your models here.
class AccountExpenses(models.Model):
   
    Date = models.DateField()
    Day =models.CharField(max_length=20)
    Toner= models.IntegerField()
    TonerSpent= models.IntegerField()


    isSunday = models.IntegerField()
    isHoliday = models.IntegerField()
    isPaperCame= models.IntegerField()
    PaperQuantityCame= models.IntegerField()
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
    PaperSheet = models.IntegerField()
    PaperPresentToday =models.IntegerField()
  
    PaperSoldToday =models.IntegerField()
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
    TajPresent = models.IntegerField()
    TajExpense = models.IntegerField()
    NoorPresent = models.IntegerField()
    NoorExpense = models.IntegerField()

    isTajHalfDay = models.IntegerField()
    isNoorHalfDay = models.IntegerField()
class RateSheet(models.Model):
    bata1 = models.IntegerField(default=90)
    bata2 = models.IntegerField(default=70)
    food= models.IntegerField(default=150)
    tajSalary = models.DecimalField(default=633.33,max_digits=9 , decimal_places=2)
    noorSalary = models.DecimalField(default=466.66,max_digits=9 , decimal_places=2)
    assanSalary = models.DecimalField(default=466.66,max_digits=9 , decimal_places=2)
    maniSalary = models.DecimalField(default=333.33,max_digits=9 , decimal_places=2)
    rasheedSalary = models.DecimalField(default=333.33,max_digits=9 , decimal_places=2)
    paperRate = models.DecimalField(default=0.50,max_digits=9 , decimal_places=2)
    tonerRate= models.DecimalField(default=800.00,max_digits=9 , decimal_places=2)
    singleRate= models.DecimalField(default=1.25,max_digits=9 , decimal_places=2)
    b2bRate= models.DecimalField(default=0.85,max_digits=9 , decimal_places=2)
    copiesPerToner = models.IntegerField(default=19000)

    tpmRent = models.DecimalField(default=516.66,max_digits=9 , decimal_places=2)
    kdmRent = models.DecimalField(default=800.00,max_digits=9 , decimal_places=2)

    currentBillKdm= models.IntegerField(default=110)
    currentBillTpm = models.IntegerField(default=110)
class MonthlyEntryKdm(models.Model):
    Month = models.CharField(max_length=200)
    Year = models.IntegerField()
    TotalIncome = models.IntegerField()
    NetProfit = models.IntegerField()
    TotalExpense = models.IntegerField()
    BlackReading = models.IntegerField()
    ColourReading = models.IntegerField()
    
    TajPresent = models.DecimalField(default=0,max_digits=9 , decimal_places=1)
    NoorPresent = models.DecimalField(default=0,max_digits=9 , decimal_places=1)
    
    
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
    PaperSent = models.IntegerField()
    isEdited = models.IntegerField()

    isExecuted = models.IntegerField()

class CombinedEntry(models.Model):
    Month = models.CharField(max_length=200)
    Year = models.IntegerField()
    TotalIncome = models.IntegerField()
    NetProfit = models.IntegerField()
    TotalExpense = models.IntegerField()
    BlackReading = models.IntegerField()
    ColourReading = models.IntegerField()
    
    PaperUsed = models.IntegerField()
    PaperCost = models.IntegerField()
    Rent = models.IntegerField()
    CurrentBill = models.IntegerField()
    LabourSalary = models.IntegerField()
    ExpenseCalculated = models.IntegerField()
    isEdited = models.IntegerField()
    isExecuted = models.IntegerField()


class PredictionData(models.Model):
    MonthString = models.CharField(max_length=200)
    
    Year = models.IntegerField()
    Paper = models.IntegerField()
    PaperPending = models.IntegerField()
    Salary = models.IntegerField()
    SalaryPending = models.IntegerField()
    Toner = models.IntegerField()
    TonerPending=  models.IntegerField()
    Kl = models.IntegerField()
    KlPending=models.IntegerField()
    Vadapalani=models.IntegerField()
    VadapalaniPending=models.IntegerField()
    David=models.IntegerField()
    DavidPending =models.IntegerField()
    RentTpm=models.IntegerField()
    RentTpmPending =models.IntegerField()
    RentAshref =models.IntegerField()
    RentAshrefPending =models.IntegerField()
    RentNoushad =models.IntegerField()
    RentNoushadPending =models.IntegerField()
    Rent2 =models.IntegerField()
    Rent2Pending =models.IntegerField()
    Current =models.IntegerField()
    CurrentPending =models.IntegerField()
    Others =models.IntegerField()
    OthersPending = models.IntegerField()






