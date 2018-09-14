#work on python2 only
import nmap
import optparse
def nmapscan(tgthost, tgtport):
    scann=nmap.PortScanner()
    scann.scan(tgthost, tgtport)
    state=scann[tgthost]['tcp'][int(tgtport)]['state']
    print(("[*]"+tgthost+"tcp/"+tgtport+":::"+state))


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
    for tgtport in tgtports:
        nmapscan(tgthost, tgtport)
if __name__ == '__main__':
    main()