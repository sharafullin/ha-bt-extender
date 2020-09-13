import time
import git
from git import Repo

repo = Repo("/opt/ha-bt-extender")
remoteRepo = Repo("/opt/ha-bt-extender-remote")

while true:
    origin = remoteRepo.remotes.origin
    origin.pull()
    time.sleep(60)