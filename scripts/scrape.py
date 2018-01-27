#!/usr/bin/python

# usage:  python search.py <IG username>

import sys
import requests
from bs4 import BeautifulSoup
import urllib2
import re
import json

test_link = "https://www.google.com/searchbyimage?&image_url=https://scontent-iad3-1.cdninstagram.com/vp/63d07260370df51f9160551f3e800185/5AF88680/t51.2885-15/e35/22582543_1924170541154740_2332192569150144512_n.jpg"

test_link2 = "https://www.google.co.uk/search?tbs=sbi:AMhZZitnsN1grwUvVjPZ-rJHTZ1r2KHpXDnac4c7adzM7mzX0faXwApX1mOGY33bmYJa76AuVHCQhJzHzgn9zDaQK20X3-JFC2MXx1hKLg9o647afy22Q7gQJkGryv6zy3AttYqCRvdyiyHZNe0-oKYZj749V4x6USU7mcUwb_1VgCKXGauRY3Cx5xpJCnyA1uWj2vAxDl4ZPAOWljDC1IU8U9jCDJlqOhfki5dPUWE3kAhPOyWU7vXk6q-e8FjPbWGLZruJzPVR7zyifH5qri31gudh7fnd52tezNwWwxotfbaO38PXJYgC_1JAPYDD6DpnW6frYvXoFkLQrio4g2RJo8M9dacTuArg&gws_rd=cr&dcr=0&ei=f8hfWtjHDc3YwAK0-JrQDA"

html_page = urllib2.urlopen(test_link2)
soup = BeautifulSoup(html_page, "html5lib")

string_json = soup.body

print string_json
