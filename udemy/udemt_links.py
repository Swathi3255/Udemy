from selenium import webdriver
from lxml import html
import time
from urllib.parse import urljoin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options

base_url = 'https://www.udemy.com/'

urls = [
'https://www.udemy.com/courses/development/',
'https://www.udemy.com/courses/finance-and-accounting',
'https://www.udemy.com/courses/it-and-software',
'https://www.udemy.com/courses/personal-development/',
'https://www.udemy.com/courses/marketing',
'https://www.udemy.com/courses/health-and-fitness'
]

#url = 'https://www.udemy.com/courses/development/'
driver = webdriver.Chrome()


def parse(url):
	driver.get(url)
	wait(driver, 30).until(EC.presence_of_element_located(
		(By.XPATH, '//div[@class="course-list--container--3zXPS"]/div[@class="popover--popover--t3rNO popover--popover-hover--14ngr"]')))
	
	attr = html.fromstring(driver.page_source)
	links = attr.xpath('//div[@class="course-list--container--3zXPS"]/div[@class="popover--popover--t3rNO popover--popover-hover--14ngr"]//@href')

	with open('done.txt','a',encoding='utf-8')as g:
		g.write(url+'\n')

	for link in links:
		print(link)
		f.write(link+'\n')

	nextPage = attr.xpath('//*[@aria-label="next page"]/../@href')
	if nextPage:
		url = urljoin(base_url,nextPage[0])
		parse(url)



with open('links.txt','a',encoding='utf-8')as f:
	for url in urls:
		parse(url)
