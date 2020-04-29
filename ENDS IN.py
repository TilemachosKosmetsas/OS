import os
import os.path
import re
buffer=[]
a= str(input("teleiwnei se "))
while 3:
        pattern = (r'^.*\.'+a+'$').strip()
        dir= input('initial folder')
        if dir == '': break
        if os.path.isdir(dir):
                for r,d,f in os.walk(dir):             
                        for fi in f :            
                                if re.search(pattern,fi,re.I) and fi.endswith(a):
                                    print (fi)
                                    #print (r)
                                                
                                                
