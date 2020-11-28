#BRUTEFORCE METHOD TO EXTRACT THE CONTACT PAGE AND PINGING EACH WEBSITE FOR 200 STATUS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge,EdgeOptions
import requests 
import xlrd
def checking_with_Ext(URL,i):
	#print(URL+"-------",i)
	contact = ["contact","contacts","contact-us","contactus"]
	extension = [".html",".php",".htm",".wpx"]

	for c in contact:
		for e in extension:
			try:
				#print(URL+"/"+c+e,"")
				if(int(requests.get("http://"+URL+"/"+c+e).status_code) == 200):
					print (URL+"/"+c+e)
			except Exception as e:
				#print(e)
				pass	
# options = EdgeOptions()
# options.use_chromium = True
# driver = Edge(options = options)
# options.headless = True
# options.add_argument('--headless')
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')
PATH = "C:/Users/karti/Downloads/sales.xlsx"
wb = xlrd.open_workbook(PATH)
sheet = wb.sheet_by_index(0)

for i in range(2,1482):
	URL = str(sheet.cell_value(i,6))
	checking_with_Ext(URL,i)



# driver.get('http://www.thetutor.in/contactus.php')
# search = driver.find_elements_by_tag_name("a")
# for i in search:
# 	print (i.text+" END OF LINE -------------------")
#print(search)
# driver.close()
