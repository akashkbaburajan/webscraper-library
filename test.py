from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import csv
def lookup(query):
	browser = webdriver.Firefox() 
	browser.get("https://www.indiabookstore.net/")
	inputElement = browser.find_element_by_name("q")
	inputElement.send_keys(query)
	
# submit the form (although google automatically searches now without submitting)
	inputElement.submit()
	try:
#browser.implicitly_wait(15)
		button=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "bookDetailsLink")))	
		button.click()
		WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "bookPageBuyLink")))
		print "done"

	finally:

		source = browser.page_source
		#print source
#print html_source
		browser.quit()

		soup = BeautifulSoup(source,'html.parser')  
	#print soup.title.string

	#print soup
#class "postText" is not defined in the source code

		booktitle = soup.find_all('div', attrs={'class':'coverImage center-align-util'})
		price =soup.find_all('div', attrs={'class':'price'})[0]
		myitems={}
		for elem in booktitle:
    			myitems["booktitle"]= elem('img')[0]['alt']
			break

			
		myitems["price"]=price.text
		writer = csv.writer(open('dict.csv', 'a'))
		for key, value in myitems.items():
  				 writer.writerow([key, value])
					

		return 
		

#for span in spans:
 #   print span.string

if __name__ == "__main__":
	
	with open('books.txt') as f:
    		for line in f:
			query=line.split('\n')
			lookup(query)
			

