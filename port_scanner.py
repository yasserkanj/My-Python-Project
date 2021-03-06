import optparse
from socket import *
from threading import *


def connscan(tgthost,tgtport):
#check every port as Thread
    screenlock=Semaphore(value=1)
    try:
        conn=socket(AF_INET,SOCK_STREAM)
        conn.connect((tgthost,tgtport))
        conn.send('heloooo \n\r')
        screenlock.acquire()
        recvv=conn.recv(1000)
        print("[+] port %d is open "%(tgtport))
        print("resaults for this port :"+str(recvv))
    except:
        screenlock.acquire()
        print("[-] port %d is close"%(tgtport))
    finally:
        screenlock.release()
        conn.close()

def portscan(tgthost,tgtports):
#check th ip and after that it calls connscan as Thread
    try:
        tgtip = gethostbyname(tgthost)
    except:
        print ("[-] Cannot resolve '%s': Unknown host"%(tgthost))
        return        
    try:
        tgtname=gethostbyaddr(tgthost)
        print("scan resaults for :"+ tgtname[0])
    except:
        print("scan resaults for :"+tgtip)
    setdefaulttimeout(1)
    print ("========================")
    for tgtport in tgtports:
        t=Thread(target=connscan,args=(tgthost,int(tgtport)))
        t.start()

def main():
    parser = optparse.OptionParser("usage %prog "+"-H <target host> -P <target port>")
    parser.add_option('-H', dest='tgthost', type='string',help='specify target host')
    parser.add_option('-P', dest='tgtport', type='string',help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgthost = options.tgthost
    tgtports = str(options.tgtport).split(",")
    if (tgthost == None) | (tgtports[0] == None):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    portscan(tgthost, tgtports)
if __name__ == '__main__':
    main()