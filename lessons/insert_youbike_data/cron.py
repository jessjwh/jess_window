from crontab import CronTab
import os
cron = CronTab(user=True)
path = os.path.abspath("./lessons2.py")
job = cron.new(command=f"/opt/anaconda3/envs/venv2/bin/python '{path}'")
job.minute.every(10)
job.set_comment("Output hello world")
cron.write()