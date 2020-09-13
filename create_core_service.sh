cat <<EOT >> ha-bt-extender-core.service
[Unit]
Description=service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/sudo /usr/bin/sudo python3 /home/ha-bt-extender/core.py

[Install]
WantedBy=multi-user.target
EOT