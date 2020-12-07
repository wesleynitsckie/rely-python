import time
import json
from base.models import Sanction
from base.models import Transaction
class SanctionCheck:

    def process(self, transaction):
        """ Check if the person is in the sanctioned list """
        #Transaction.objects.filter(id=transaction.id).update(status=Transaction.Status.SANCTIONCHECK)
        #transaction = Transaction.objects.get(id=trans.id)
        print("The transaction.save() ran")
        person = json.loads(transaction.transaction_blob)
        result = Sanction.objects.filter(
            first_name=person['first_name'],
            last_name=person['last_name'],
            dob=person['dob']
        )
        
        if result.count() > 0:
            transaction.is_person_on_sanction_list= True
            transaction.status = Transaction.Status.SANCTIONCHECKCOMPLETED
            
        else:
            transaction.is_person_on_sanction_list= False
            transaction.status=Transaction.Status.PEPCHECK
            print(transaction.is_person_on_sanction_list)
        transaction.save()
        time.sleep(10)
        print("Sanction Check completed :::: status {}::: is_person_on_sanction_list: {}".format(transaction.status,transaction.is_person_on_sanction_list ))