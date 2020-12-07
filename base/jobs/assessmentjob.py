import multiprocessing
from base.services.riskassessment import AssessmentCheck
import time

class AssessmentJob:
    """ Assessment Job processes the asyncronously """
    def __init__(self, transaction):
        self.transaction = transaction
        self.proc = multiprocessing.Process(target=self.worker)

    def worker(self):
        """work function"""
        print("Assessment Worker Running")
        assessment_check = AssessmentCheck()
        assessment_check.process(self.transaction)
        print("Assessment Worker Complete")
        return

    def run(self):
        self.proc.start()
        
        