import time, sched
from multiprocessing import Process, Queue
import udp_discovery
import tcp_discovery

logger = Queue()
q = Queue()

def heartbeat():
    print(time.time(), "heartbeat")
    while not logger.empty():
        data = logger.get(timeout=0.5)
        print("log: ", data)

s = sched.scheduler(time.time, time.sleep)
s.enter(30, 1, heartbeat)

logger.put("started of internal service")
udp_discovery_process = Process(target=udp_discovery.start_udp_discovery, args=(logger,))
udp_discovery_process.start()
tcp_discovery_process = Process(target=tcp_discovery.start_tcp_discovery, args=(logger, q))
tcp_discovery_process.start()

s.run()

udp_discovery_process.join()
tcp_discovery_process.join()