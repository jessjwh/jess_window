from crontab import CronTab
import os
cron = CronTab(user=True)
path = os.path.abspath("./lessons2.py")
job = cron.new(command=f"python '{path}'")
job.minute.every(10)
cron.write()