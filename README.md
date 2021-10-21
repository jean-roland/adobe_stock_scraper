# Adobe Soock Scrapper

A python/selenium scrapper for Adobe Stock Image thumbnails I quickly made for an IA project I have.

## Pre-requisite
(Just in case)
* Install [Python3](https://www.python.org/downloads/).
* Install [Google Chrome](https://www.google.com/intl/fr_fr/chrome/).

* Download the correct [chromedriver](https://chromedriver.chromium.org/downloads) for your OS and Chrome version.
* Install selenium `pip install selenium`.
* Install beautiful soup `pip install beautifulsoup4`.
* Find the url on [Adobe Stock](https://stock.adobe.com/ch_fr/) containing the images you want, by making a search request by example.

## How to use
You must first configure the script under the `# Script params` comment:
* The path to your chromedriver in `DRIVER_PATH`.
* The path to the directory where images will be stored in `scrape_directory`(the script will try to create one if it doesn't exist).
* The url that will be used to scrap images in `base_url`.
* The maximum number of pages to go through in `page_max` (for the [example url](https://stock.adobe.com/fr/collections/Pnb3vT0akesPgEDqaqSlBRifOFBa3LoJ) I set up there is a maximum of 4 pages as displayed at the bottom, you might want less than the maximum though).
* (optionnal) the starting page (default is the first one) in `page_start` (in case you want to start at a given page or if you had to interrupt the script and don't want to start from the beginning).

Once the configuration is done you just need to launch the script:
* Open a shell in the directory containing the script
* Use the command `python scrapper.py`

The selenium chrome should launch and do his thing.

If you encounter any bugs or issues feel free to contact me at jean.roland.gosse@gmail.com
