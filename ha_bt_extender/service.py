import time, git, os, json
from git import Repo
from multiprocessing import Process, Queue
import udp_discovery
import tcp_discovery
import netifaces as ni

from configuration_managers.climate.eq3btsmart import Eq3BtSmartConfig

repo = Repo("/opt/ha-bt-extender")
origin = repo.remotes.origin
origin.pull()

remoteRepo = Repo("/opt/ha-bt-extender-remote")

devices = []
q = Queue()

def heartbeat():
    print(time.time(), "heartbeat")

    remoteOrigin = remoteRepo.remotes.origin
    remoteOrigin.pull()
    if repo.active_branch.commit.hexsha != remoteRepo.active_branch.commit.hexsha:
        os.system('reboot')

    ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

    while not q.empty():
        data = q.get(timeout=0.5)
        print("data: ", data)
        if data == "":
            devices.clear()
        else:
            conf = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            print("dev mac:", conf.mac)
            print("dev config:", conf.configuration)
            found_devices = scanner.scan(10.0)
            for found_device in found_devices:
                if found_device.addr == conf.mac:
                    device = Eq3BtSmartConfig("homeassistant", ip, found_device)
                    device.configure(conf.configuration)
                    devices.append(device)
        print("devices: ", devices)
    s.enter(30, 1, heartbeat)
    for device in devices:
        device.refresh()
        print("name: ", device.device.name)
        print("available: ", device.device.available)

s = sched.scheduler(time.time, time.sleep)
s.enter(30, 1, heartbeat)

udp_discovery_process = Process(target=udp_discovery.start_udp_discovery)
udp_discovery_process.start()

tcp_discovery_process = Process(target=tcp_discovery.start_tcp_discovery, args=(q,))
tcp_discovery_process.start()

s.run()

udp_discovery_process.join()
tcp_discovery_process.join()