import multiprocessing
from base.services.pepcheck import PEPCheck
import time
class PEPJob:
    
    def __init__(self, transaction):
        self.transaction = transaction
        self.proc = multiprocessing.Process(target=self.worker)

    def worker(self):
        """work function"""
        print("PEP Worker Running")
        sanction_check = PEPCheck()
        sanction_check.process(self.transaction)
        print("PEP Worker Complete")
        return

    def run(self):
        self.proc.start()
        
        