#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import sys
from math import ceil

BASE_URL='http://www.alexa.com/topsites/countries;%d/%s'

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: COUNTRY-CODE TOP-N\n')
        sys.exit(1)
    
    country_code = sys.argv[1].upper()
    number = int(sys.argv[2])
    delimiter = ' '

    page_numbers = int(ceil(number/50.0))

    for page_num in range(0, page_numbers): 
        print "Getting URL:" + BASE_URL % (page_num, country_code)
        response = requests.get(BASE_URL % (page_num, country_code))  
    
        soup = BeautifulSoup(response.text, "html.parser")
        bullets = soup.find_all('div', {'class':'tr site-listing'})
    
        for bullet in bullets:
            acell = bullet.find('div', {'class':'td DescriptionCell'})
            rank = bullet.div.contents[0]
            site = acell.p.a.contents[0]
            print('%s%s%s' % (rank, delimiter, site))
            