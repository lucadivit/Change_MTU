from Iface import Iface

iface = Iface("wlan0")
iface.set_mtu(2000)
iface.restore_mtu()