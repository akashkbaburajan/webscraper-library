# webscraper-library


------------------------------------------------edit-Getpriceofbooks--------------------




To scrape a webpage and acquire price details of all the required books .(book names provided as a text file books.txt)

prerequisite:
  1.python 2.7 installed
  2.install pip using the terminal:sudo apt-get install python-pip
  
  
  
  Using virtualenv allows you to install the Selenium Python bindings (and any other Python modules you might want) into an isolated environment, rather than the global packages dir, which (among other benefits) can help make your test environment easily reproducible on other machines:
  
  
  3.installing virtualenv:sudo pip install virtualenv

  4.Create a dir in which to install your virtualenv environment, and install and activate a new env
  
   bill@ubuntu:~$ mkdir mytests && cd $_

  bill@ubuntu:~/mytests$ virtualenv env

  bill@ubuntu:~/mytests$ . env/bin/activate
  
  5.Install the Selenium bindings for Python

  (env)bill@ubuntu:~/mytests$ pip install selenium
  
  6.Install beautifulsoup4
  
  (env)bill@ubuntu:~/mytests$ pip install beautifulsoup4
   
  refer the following site for more info:
    http://blog.likewise.org/2015/01/setting-up-chromedriver-and-the-selenium-webdriver-python-bindings-on-ubuntu-14-dot-04/
    
    Download the GetBooksByPrice.py file and run it in the virtual environment.
    
    (env)bill@ubuntu:~/mytests$ python GetBooksByPrice.py
    
    
