import re         
import time
from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup

 
url="http://www.resonance.ac.in"
req = Request(url)
html = urlopen(req).read()
html=html.decode()
bsObj = BeautifulSoup(html,features="lxml");
links=[]
for link in bsObj.find_all('a'):
    links.append(str(link.get('href')))
    #print(url + str(link.get('href')))
 

def Email(url):
    try:
        req = Request(url)
        hh = urlopen(req).read() 
        time.sleep(0.5)
        #time.sleep(1)
    #raw_html=t.text
    #dd=html2text.html2text(hh)
        dd=hh.decode()
        email=re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',dd)   
        email = list(dict.fromkeys(email))                                                                                                            # this is email format
        print(email)
        phone=re.findall(r'\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})',dd)  
        #print(phone)
        for ph in phone:
            if(ph[0]=='' and (ph[1].startswith('09') or ph[1].startswith('9'))):
                print(ph[1:4])
     #  print()
    #links.remove(url)
    except:
       pass
for b in links:
    Email(b)
    time.sleep(0.5)
