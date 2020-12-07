import multiprocessing
from base.services.sanctioncheck import SanctionCheck
import time
class SanctionJob:
    
    def __init__(self, transaction):
        self.transaction = transaction
        self.proc = multiprocessing.Process(target=self.worker)

    def worker(self):
        """work function"""
        print("Worker Running")
        sanction_check = SanctionCheck()
        sanction_check.process(self.transaction)
        print("Worker Complete")
        return

    def run(self):
        self.proc.start()
        
        