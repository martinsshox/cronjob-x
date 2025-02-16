from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class ManagerCron:
    def __init__(self):
        self._jobs = []
        self._scheduler = AsyncIOScheduler()
        
    def add_job(self, job):
        self._jobs.append(job)
        
    def run(self):
        for job in self._jobs:
            self._scheduler.add_job(job.initialize, 'interval', seconds=10)
            
        self._scheduler.start()
        
        print(rf"""
                   
            ,---.  .-. .-..-. .-..-. .-.,-..-. .-.  ,--,   
            | .-.\ | | | ||  \| ||  \| ||(||  \| |.' .'    
            | `-'/ | | | ||   | ||   | |(_)|   | ||  |  __ 
            |   (  | | | || |\  || |\  || || |\  |\  \ ( _)
            | |\ \ | `-')|| | |)|| | |)|| || | |)| \  `-) )
            |_| \)\`---(_)/(  (_)/(  (_)`-'/(  (_) )\____/ 
                (__)     (__)   (__)      (__)    (__)     
            {len(self._jobs)} job at: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
        """)