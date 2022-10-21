from rest_framework import viewsets
from . import models
from . import serializers

class AccountExpensesViewset3(viewsets.ModelViewSet):
    queryset = models.AccountExpenses.objects.all()
    serializer_class = serializers.AccountExpensesSerializer


class RateSheetViewset3(viewsets.ModelViewSet):
    queryset = models.RateSheet.objects.all()
    serializer_class = serializers.RateSheetSerializer