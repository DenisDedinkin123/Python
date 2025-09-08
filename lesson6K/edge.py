import msedgedriver

from selenium import webdriver



msedgedriver.install() #you will notice a file named msedgedriver.exe is downloaded in your directory



Driver = webdriver.Edge('msedgedriver.exe')#msedgedriver was installed by above command

