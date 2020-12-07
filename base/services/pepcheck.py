import time
import json
from base.models import PEP
from base.models import Transaction
class PEPCheck:

    def process(self, transaction):
        """ Check if the person is in the PEP list """
        print('PEP Check started {}'.format(transaction.id ))
        
        person = json.loads(transaction.transaction_blob)
        result = PEP.objects.filter(
            first_name=person['first_name'],
            last_name=person['last_name']
        )
        
        if result.count() > 0:
                transaction.is_person_on_pep_list= True
                transaction.status=Transaction.Status.PEPCHECKCOMPLETED
        else:
                transaction.is_person_on_pep_list= True
                transaction.status=Transaction.Status.ASSESSMENT
        transaction.save()
        time.sleep(10)

        print('PEP Check completed')