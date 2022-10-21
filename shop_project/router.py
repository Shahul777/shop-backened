from shopAccountKdm.viewsets import AccountExpensesViewset,LabourExpensesViewset,RateSheetViewset

from houseAccount.viewsets import AccountExpensesViewset3,RateSheetViewset3
from shopAccountTpm.viewsets import AccountExpensesViewset2,LabourExpensesViewset2
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', AccountExpensesViewset)
router.register('labours', LabourExpensesViewset)

router.register('accounts2', AccountExpensesViewset2)
router.register('labours2', LabourExpensesViewset2)


router.register('rate', RateSheetViewset)


router.register('accounts3', AccountExpensesViewset3)



router.register('rate3', RateSheetViewset3)
