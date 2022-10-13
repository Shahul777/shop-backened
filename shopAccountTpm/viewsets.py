from rest_framework import viewsets
from . import models
from . import serializers


class AccountExpensesViewset2(viewsets.ModelViewSet):
    queryset = models.AccountExpenses.objects.all()
    serializer_class = serializers.AccountExpensesSerializer

class LabourExpensesViewset2(viewsets.ModelViewSet):
    queryset = models.LabourExpenses.objects.all()
    serializer_class = serializers.LabourExpensesSerializer