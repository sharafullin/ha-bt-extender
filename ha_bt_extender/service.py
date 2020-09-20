import time, git, os
from git import Repo
from multiprocessing import Process, Queue
import internal_process


repo = Repo("/opt/ha-bt-extender")
origin = repo.remotes.origin
origin.pull()

remoteRepo = Repo("/opt/ha-bt-extender-remote")

os.system('pip3 install -r /opt/ha-bt-extender/requirements.txt')

os.system('systemctl start ha-bt-extender-internal')

logger = Queue()

internal_process = Process(target=internal_process.start, args=(logger,))
internal_process.start()

while True:
    remoteOrigin = remoteRepo.remotes.origin
    remoteOrigin.pull()
    if repo.active_branch.commit.hexsha != remoteRepo.active_branch.commit.hexsha:
        os.system('reboot')
    
    while logger.full():
        print(logger.get())

    time.sleep(60)

internal_process.join()