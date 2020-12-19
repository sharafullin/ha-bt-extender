import time, git, os
import logging
from git import Repo
from multiprocessing import Process, Queue

logging.basicConfig(level="INFO")
logging.info('test')
repo = Repo("/opt/ha-bt-extender")

remoteRepo = Repo("/opt/ha-bt-extender-remote")

print('python3.7 -m pip install -r /opt/ha-bt-extender/requirements.txt')
os.system('python3.7 -m pip install -r /opt/ha-bt-extender/requirements.txt')

print('systemctl start ha-bt-extender-internal')
os.system('systemctl start ha-bt-extender-internal')
print('ha-bt-extender-internal started')
logger = Queue()

while True:
    remoteOrigin = remoteRepo.remotes.origin
    remoteOrigin.pull()
    if repo.active_branch.commit.hexsha != remoteRepo.active_branch.commit.hexsha:
        origin = repo.remotes.origin
        origin.pull()
        os.system('reboot')
    
    while logger.full():
        print(logger.get())

    time.sleep(60)
