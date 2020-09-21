import time, git, os
from git import Repo
from multiprocessing import Process, Queue

repo = Repo("/opt/ha-bt-extender")

remoteRepo = Repo("/opt/ha-bt-extender-remote")

os.system('python3.7 -m pip install -r /opt/ha-bt-extender/requirements.txt')

os.system('systemctl start ha-bt-extender-internal')

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
