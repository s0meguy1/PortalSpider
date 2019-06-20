#!/bin/bash
# Start
echo "to see IP leases, use this command:"
echo "cat /var/lib/misc/dnsmasq.leases"
echo "to edit wifi, go here: /etc/hostapd/hostapd.conf"
#airmon-ng check
killall wpa_supplicant
# Configure IP address for WLAN
sudo ifconfig wlan0 192.168.150.1
# Start DHCP/DNS server
sudo service dnsmasq restart
# Enable routing
sudo sysctl net.ipv4.ip_forward=1
# Enable NAT
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -j ACCEPT
# Run access point daemon
sudo hostapd /etc/hostapd/hostapd.conf
# Stop
# Disable NAT
sudo iptables -D POSTROUTING -t nat -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -j ACCEPT
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
# Disable routing
sudo sysctl net.ipv4.ip_forward=0
# Disable DHCP/DNS server
sudo service dnsmasq stop
sudo service hostapd stop
