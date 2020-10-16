import time, sched, logging
from multiprocessing import Process, Queue
import udp_discovery
import tcp_discovery

logging.basicConfig(level="INFO")

logger = Queue()
q = Queue()
logging.info("Service started")

def heartbeat():
    logging.info("heartbeat")
    while not logger.empty():
        data = logger.get(timeout=0.5)
        logging.info(data)


s = sched.scheduler(time.time, time.sleep)
s.enter(30, 1, heartbeat)

udp_discovery_process = Process(target=udp_discovery.start_udp_discovery, args=(logger,))
udp_discovery_process.start()
tcp_discovery_process = Process(target=tcp_discovery.start_tcp_discovery, args=(logger, q))
tcp_discovery_process.start()

s.run()

udp_discovery_process.join()
tcp_discovery_process.join()