from django.contrib import admin

# Register your models here.
from shopAccountTpm.models import AccountExpenses, LabourExpenses,MonthlyEntryTpm
# Register your models here.
admin.site.register(AccountExpenses)
admin.site.register(LabourExpenses)
admin.site.register(MonthlyEntryTpm)