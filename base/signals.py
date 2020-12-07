from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
from .jobs.sanctionjob import SanctionJob
from .jobs.pepjob import PEPJob
from .jobs.assessmentjob import AssessmentJob

""" 
Signals gets triggered when there are 
any saves to the database.
"""


@receiver(post_save, sender=Transaction)
def process_transaction(sender, instance, created, **kwarks):
    if created:
        # Lets kick off the first process
        print("POST SAVE CREATED")
        sanctionJob = SanctionJob(transaction=instance)
        sanctionJob.run()
    else:
        # Check where we are in the process
        print ("POST SAVE UPDATED {} {}".format(instance.id, instance.status))
        if instance.status == Transaction.Status.PEPCHECK:
            print('Starting PEP job')
            pepjob = PEPJob(transaction=instance)
            pepjob.run()
        elif instance.status == Transaction.Status.ASSESSMENT:
            print('Starting Assessment job')
            assessmentjob = AssessmentJob(transaction=instance)
            assessmentjob.run()