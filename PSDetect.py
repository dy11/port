#coding:utf-8
from scapy.layers.inet import *
import threading
import time
import signal

hostlist = {}

def t1():
    hostlist.clear()
    print "test"
def t2():
    while 1:
        t1()
        time.sleep(5)

def quit(signum,frame):
    print "quit!"
    print hostlist
    os._exit(signum)
def timestamp2time(timestamp):
    timeArray = time.localtime(timestamp)
    mytime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return mytime

def packet_callback(packet):
    if packet[IP].src not in hostlist:
        hostlist[packet[IP].src] = 1
    else:
        hostlist[packet[IP].src]+=1
        if hostlist[packet[IP].src] >= 30:
            print "Scanner detected. The Scanner originated from %s"% packet[IP].src
if __name__ == "__main__":
    #print 'test'
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        t = threading.Thread(target=t2)
        t.start()
        sniff(filter="tcp",prn = packet_callback)
        t.join()
    except Exception, exc:
        print exc
