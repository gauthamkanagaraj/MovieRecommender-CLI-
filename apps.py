from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
print("")
print("")
mood = input("How are you feeling today? ")
streaming = input("What is your preferred streaming platform? ")
titles = []
movietitles = []

def searching():
	try:
		movies = driver.find_element_by_tag_name("main")
		table = movies.find_element_by_tag_name("tbody")
		rows = table.find_elements_by_tag_name("tr")

		for row in rows:
			title = row.find_element_by_class_name("css-1u7zfla")
			titles.append(title.text)

	except:
		print("Error in Clicking Loading")

	random1, random2, random3 = random.sample(titles, 3)
	movietitles.append(random1)
	movietitles.append(random2)
	movietitles.append(random3)
	print("")
	print("")
	print("Your Recommendations are: " + movietitles[0] + "," + movietitles[1] + "," + movietitles[2])

if(mood == 'happy' and streaming == 'netflix'):
	driver = webdriver.Chrome(executable_path=PATH)
	driver.get('https://reelgood.com/movies/genre/comedy/on-netflix')
	searching()

elif(mood == 'happy' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/comedy/on-amazon')
	searching()
elif(mood == 'sad' and streaming == 'netflix'):
	driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
	searching()
elif(mood == 'sad' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
	searching()
elif(mood == 'excited' and streaming == 'netflix'):
	driver.get('https://reelgood.com/movies/genre/thriller/on-netflix')
	searching()
elif(mood == 'excited' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/thriller/on-amazon')
	searching()
elif(mood == 'angry' and streaming == 'netflix'):
	driver.get('https://reelgood.com/movies/genre/drama/on-netflix')
	searching()
elif(mood == 'angry' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/drama/on-amazon')
	searching()
elif(mood == 'loved' and streaming == 'netflix'):
	driver.get('https://reelgood.com/movies/genre/romance/on-netflix')
	searching()
elif(mood == 'loved' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/romance/on-amazon')
	searching()
elif(mood == 'depressed' and streaming == 'netflix'):
	driver.get('https://reelgood.com/movies/genre/fantasy/on-netflix')
	searching()
elif(mood == 'depressed' and streaming == 'prime'):
	driver.get('https://reelgood.com/movies/genre/fantasy/on-amazon')
	searching()