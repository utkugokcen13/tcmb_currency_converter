# Effective dollar value will be taken from the TCMB website.

# https://www.turkiye.gov.tr/doviz-kurlari

from bs4 import *
import requests

site = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")

soup = BeautifulSoup(site.text, "html.parser")

efektif_dolar_satis = soup.find('td', text='1 ABD DOLARI').find_next_sibling('td')\
                                                          .find_next_sibling('td')\
                                                          .find_next_sibling('td')\
                                                          .find_next_sibling('td').text

print(efektif_dolar_satis)