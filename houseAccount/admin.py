from django.contrib import admin
from houseAccount.models import AccountExpenses, RateSheet

# Register your models here.
admin.site.register(AccountExpenses)

admin.site.register(RateSheet)