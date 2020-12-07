import time
import json
from base.models import Transaction

class AssessmentCheck:

    def process(self, transaction):
        """ Let do the Assessment """
        print('Assessment Check started')
        person = json.loads(transaction.transaction_blob)
        if transaction.is_person_on_pep_list == False:
            # Approve if the person is not on any list
            status = Transaction.Status.ACCEPTED
        else:
            # On a list but income more than 25k
            if person["income"] > 25000:
                status = Transaction.Status.DENIED
            else:
                status = Transaction.Status.ACCEPTED

        transaction.status = status
        transaction.save()
        time.sleep(10)
        print('Assessment Check completed ' + transaction.status)