import itertools
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file', action="store", dest="userfile", help="File containing keywords", default=False)
parser.add_option('-d', '--dictionary', action="store", dest="dictionary", help="File containing permutations", default=False)
parser.add_option('-l', '--length', action="store", dest="minlen", help="Minimum Length", default=True)
options, args = parser.parse_args()
if (options.minlen is None):
		plen=3
else:
    plen = int(options.minlen)
    print 'Using Min pass length %d ' %plen 

if (options.userfile == False):
    print "Please specify input keyword file"
    exit()
if (options.dictionary == False):
    print 'You have to set a valid path for the passwords dictionary'
    exit()

f=open(options.userfile,'r')
list=f.read().splitlines()
print len(list)
d=open(options.dictionary,'w')
for i in range(0,len(list)):
    if len(list[i])>plen:
        d.write(list[i]+'\n')
e = 2
for p in itertools.permutations(list, e):
        wrd=p[0]+p[1]
        print wrd
        if len(wrd)>plen:
            d.write(wrd+'\n')
d.close()        