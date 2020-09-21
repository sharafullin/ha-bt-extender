sudo cat <<EOT >> /lib/systemd/system/ha-bt-extender.service
[Unit]
Description=service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/sudo /usr/bin/sudo python3.7 /opt/ha-bt-extender/ha_bt_extender/service.py

[Install]
WantedBy=multi-user.target
EOT

sudo cat <<EOT >> /lib/systemd/system/ha-bt-extender-internal.service
[Unit]
Description=service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/sudo /usr/bin/sudo python3.7 /opt/ha-bt-extender/ha_bt_extender/internal_service.py

[Install]
WantedBy=multi-user.target
EOT