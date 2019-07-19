from Iface import Iface

iface = Iface("wlan0")
iface.set_mtu(2000)
print(iface.get_mtu())
iface.restore_mtu()
print(iface.get_mtu())
