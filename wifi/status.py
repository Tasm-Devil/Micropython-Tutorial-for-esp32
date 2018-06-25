import network
sta_if = network.WLAN(network.STA_IF)
print(sta_if.ifconfig())
