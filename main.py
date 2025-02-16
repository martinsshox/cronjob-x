import asyncio
from source.config.Env import Env
from source.cron.ManagerCron import ManagerCron
from source.cron.jobs.discloud.DiscloudJob import DiscloudJob
from source.http.discloud.DiscloudClient import DiscloudClient

managerCron = ManagerCron()

discloudClient = DiscloudClient(Env.DISCLOUD_API_TOKEN)
discloudJob = DiscloudJob(discloudClient, "shox")

managerCron.add_job(discloudJob)
managerCron.run()

asyncio.get_event_loop().run_forever()