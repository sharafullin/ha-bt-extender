sudo apt-get update && sudo apt-get --assume-yes install python3.7 && sudo apt --assume-yes install python3-pip && mkdir -p /opt/ha-bt-extender && git clone -q https://github.com/sharafullin/ha-bt-extender.git /opt/ha-bt-extender && pip3 install -r /opt/ha-bt-extender/requirements.txt 


#pip3 install git+git://github.com/sharafullin/ha-bt-extender.git#egg=ha-bt-extender &&
