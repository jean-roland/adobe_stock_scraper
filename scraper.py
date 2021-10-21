import re
import os
import time
import ssl
import requests
import lxml
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from pathlib import Path
import selenium
from selenium import webdriver

def scroll_down(driver):
    page_height = driver.execute_script("return document.body.scrollHeight")
    total_scrolled = 0
    for i in range(page_height):
        driver.execute_script(f'window.scrollBy(0,{i});')
        total_scrolled += i
        if total_scrolled >= page_height/2:
            last_no = i
            break

    for i in range(last_no, 0, -1):
        driver.execute_script(f'window.scrollBy(0,{i});')

def imagescrape():
    try:
        # Script params
        DRIVER_PATH = './chromedriver.exe' # path to chromedriver
        output_dir = './output' # path to output
        base_url = 'https://stock.adobe.com/fr/search?gallery_id=Pnb3vT0akesPgEDqaqSlBRifOFBa3LoJ' # url to the images
        page_max = 4 # Max nb of page to scroll
        page_start = 1 # In case you want to resume
        # Create output directory if needed
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        # Script start
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        total_img = 0
        for i in range(page_start, page_max+1):
            url = base_url + '&search_page=' + str(i)
            driver.get(url)
            scroll_down(driver)
            data = driver.execute_script('return document.documentElement.outerHTML')
            scraper = BeautifulSoup(data, 'lxml')
            img_container = scraper.find_all('img', src=re.compile('.jpg'))
            nb_img = len(img_container) - 1
            total_img += nb_img
            print(f'Page {i} {nb_img} {total_img}')
            for j in range(0, nb_img):
                 img_src = img_container[j].get('src')
                 name = img_src.rsplit('/', 1)[-1]
                 try:
                    urlretrieve(img_src, os.path.join(output_dir, os.path.basename(img_src)))
                    #print(f'Scraped {name}')
                 except Exception as e:
                     print(e)
        driver.close()
    except Exception as e:
        print(e)


def main() -> None:
    imagescrape()


if __name__ == '__main__':
    main()
