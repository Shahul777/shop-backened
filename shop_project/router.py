from shopAccountKdm.viewsets import AccountExpensesViewset,LabourExpensesViewset,RateSheetViewset
from shopAccountTpm.viewsets import AccountExpensesViewset2,LabourExpensesViewset2
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', AccountExpensesViewset)
router.register('labours', LabourExpensesViewset)

router.register('accounts2', AccountExpensesViewset2)
router.register('labours2', LabourExpensesViewset2)


router.register('rate', RateSheetViewset)