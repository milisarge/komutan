from scapy.all import *
 
def pkt_callback(pkt):
    pkt.show() # debug statement
 
sniff(iface="enp1s0",
   prn=pkt_callback, filter="ip", store=0)
