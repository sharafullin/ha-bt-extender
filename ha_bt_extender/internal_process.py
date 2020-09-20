from multiprocessing import Process, Queue
import udp_discovery
import tcp_discovery

def start(logger: Queue):
    logger.put("started of internal process")
    udp_discovery_process = Process(target=udp_discovery.start_udp_discovery, args=(logger,))
    udp_discovery_process.start()
    tcp_discovery_process = Process(target=tcp_discovery.start_tcp_discovery, args=(logger,))
    tcp_discovery_process.start()

    udp_discovery_process.join()
    tcp_discovery_process.join()