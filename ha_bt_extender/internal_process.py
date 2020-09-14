from multiprocessing import Process
import udp_discovery

def start():
    udp_discovery_process = Process(target=udp_discovery.start_udp_discovery)
    udp_discovery_process.start()