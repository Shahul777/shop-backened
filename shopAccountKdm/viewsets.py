from rest_framework import viewsets
from . import models
from . import serializers

class AccountExpensesViewset(viewsets.ModelViewSet):
    queryset = models.AccountExpenses.objects.all()
    serializer_class = serializers.AccountExpensesSerializer

class LabourExpensesViewset(viewsets.ModelViewSet):
    queryset = models.LabourExpenses.objects.all()
    serializer_class = serializers.LabourExpensesSerializer
class RateSheetViewset(viewsets.ModelViewSet):
    queryset = models.RateSheet.objects.all()
    serializer_class = serializers.RateSheetSerializer