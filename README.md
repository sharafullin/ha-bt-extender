# ha-bt-extender

installation for ubuntu:
wget --no-cache -O - https://raw.githubusercontent.com/sharafullin/ha-bt-extender/master/install-ubuntu.sh | sudo bash

installation for raspberry pi zero
wget --no-cache -O - https://raw.githubusercontent.com/sharafullin/ha-bt-extender/master/install-raspberrypi.sh | sudo bash

Configuration of HA

1. Install MQTT (Mosquitto broker)
2. Update configuration to allow anonym access
2. Update configuration 
mqtt:
  broker: 192.168.1.100
