# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')


for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# # Set the URL you want to webscrape from
# url = 'http://web.mta.info/developers/turnstile.html'

# # Connect to the URL
# response = requests.get(url)
#
# # Parse HTML and save to BeautifulSoup object¶
# soup = BeautifulSoup(response.text, "html.parser")
#
# # To download the whole data set, let's do a for loop through all a tags
# line_count = 1  # variable to track what line you are on
# for one_a_tag in soup.findAll('a'):  # 'a' tags are for links
#     if line_count >= 36:  # code for text files starts at line 36
#         link = one_a_tag['href']
#         download_url = 'http://web.mta.info/developers/' + link
#         print(download_url)
#         urllib.request.urlretrieve(download_url, './' + link[link.find('/turnstile_')+1:])
#         time.sleep(1)  # pause the code for a sec
#     # add 1 for next line
#     line_count += 1