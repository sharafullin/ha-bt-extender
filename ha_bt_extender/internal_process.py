from multiprocessing import Process
import udp_discovery

def start():
    print("started of internal process")
    udp_discovery_process = Process(target=udp_discovery.start_udp_discovery)
    udp_discovery_process.start()

    udp_discovery_process.join()