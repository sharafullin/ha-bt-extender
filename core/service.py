import time
import git
from git import Repo
import os

repo = Repo("/opt/ha-bt-extender")
origin = repo.remotes.origin
origin.pull()

remoteRepo = Repo("/opt/ha-bt-extender-remote")

while true:
    remoteOrigin = remoteRepo.remotes.origin
    remoteOrigin.pull()
    if repo.active_branch.commit.hexsha != remoteRepo.active_branch.commit.hexsha:
        os.system('reboot')

    time.sleep(60)