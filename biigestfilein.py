import os
import os.path

s = 0
file=()
for (r,d,f) in os.walk('C:'):
    for fi in f: 
        fs = os.path.getsize(os.path.join(r,fi))
        
        if  fs > s:
                s = fs
                file = os.path.join(r,fi)
print('{:1.2f}'.format(s/1024**3))
print (file)
