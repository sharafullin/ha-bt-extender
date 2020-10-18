import time, sched, logging
from multiprocessing import Process, Queue
import udp_discovery
import tcp_discovery
import sqlite3
from collections import namedtuple

DB_NAME = "hassio"
SQL_FILE_NAME = "schema.sql"
schema=""
with open(SQL_FILE_NAME, 'r') as schema_file:
    schema=schema_file.read().replace('\n', '')
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()
sqlite3.complete_statement(schema)
curs.executescript(schema)
curs.close()
conn.close()

logging.basicConfig(level="INFO")

logger = Queue()
q = Queue()
logging.info("Service started")

def heartbeat():
    logging.info("heartbeat")
    while not logger.empty():
        data = logger.get(timeout=0.5)
        logging.info(data)

    conn = sqlite3.connect(DB_NAME)
    curs = conn.cursor()
    while not q.empty():
        data = q.get(timeout=0.5)
        if data.startswith("configure_device"):
            conf_str = data[data.index(":") + 1:]
            conf = json.loads(conf_str, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            curs.executescript('INSERT INTO devices(mac) VALUES "' + conf.mac + '"')

    curs.close()
    conn.close()

    s.enter(30, 1, heartbeat)


s = sched.scheduler(time.time, time.sleep)
s.enter(30, 1, heartbeat)

udp_discovery_process = Process(target=udp_discovery.start_udp_discovery, args=(logger,))
udp_discovery_process.start()
tcp_discovery_process = Process(target=tcp_discovery.start_tcp_discovery, args=(logger, q))
tcp_discovery_process.start()

logging.info("s.run")
s.run()

udp_discovery_process.join()
tcp_discovery_process.join()