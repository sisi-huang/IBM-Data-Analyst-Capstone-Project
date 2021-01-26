# Import libraries
import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://www.monster.de/jobs/suche/?q=Data-analyst&cy=DE&rad=20&intcid=swoop_HeroSearch_DE'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')
job_elems = results.find_all('section', class_='card-content')

csv_file = open('job_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'company', 'location'])

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
    csv_writer.writerow([title_elem.text.strip(), company_elem.text.strip(),location_elem.text.strip()])

csv_file.close()