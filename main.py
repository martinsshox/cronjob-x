import asyncio
from source.config.Env import Env
from source.cron.ManagerCron import ManagerCron
from source.clients.discloud.DiscloudClient import DiscloudClient
from source.cron.jobs.discloud.DiscloudCronJob import DiscloudCronJob

managerCron = ManagerCron()

discloudClient = DiscloudClient(Env.DISCLOUD_API_TOKEN)
discloudCronJob = DiscloudCronJob(discloudClient, "shox")

managerCron.add_job(discloudCronJob)
managerCron.run()

asyncio.get_event_loop().run_forever()