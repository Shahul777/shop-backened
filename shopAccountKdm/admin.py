from django.contrib import admin
from shopAccountKdm.models import AccountExpenses, LabourExpenses,RateSheet,MonthlyEntryKdm,CombinedEntry

# Register your models here.
admin.site.register(AccountExpenses)
admin.site.register(LabourExpenses)
admin.site.register(RateSheet)
admin.site.register(MonthlyEntryKdm)
admin.site.register(CombinedEntry)