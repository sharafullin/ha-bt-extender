sudo cat <<EOT >> /lib/systemd/system/ha-bt-extender-core.service
[Unit]
Description=service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/sudo /usr/bin/sudo python3 /opt/ha-bt-extender/core/service.py

[Install]
WantedBy=multi-user.target
EOT