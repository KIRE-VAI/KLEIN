#<\>!python3.11
#<\>coded by SAKIN
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/itz.Meh.Your.Dad')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf klein.so')
except:
    pass
os.system('rm -rf klein.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('xd.so'):
        os.system('curl -L https://github.com/SAKINXD/KLEIN/blob/main/klein.cpython-311.so?raw=true -o klein.so') 
        import klein  
    else:
        import klein
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
