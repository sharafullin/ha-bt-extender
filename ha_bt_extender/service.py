import time, git, os
from git import Repo
from multiprocessing import Process

repo = Repo("/opt/ha-bt-extender")
origin = repo.remotes.origin
origin.pull()

remoteRepo = Repo("/opt/ha-bt-extender-remote")

os.system('pip3 install -r /opt/ha-bt-extender/requirements.txt')

while True:
    remoteOrigin = remoteRepo.remotes.origin
    remoteOrigin.pull()
    if repo.active_branch.commit.hexsha != remoteRepo.active_branch.commit.hexsha:
        os.system('reboot')
    
    time.sleep(60)