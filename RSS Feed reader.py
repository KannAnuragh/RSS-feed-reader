from bs4 import BeautifulSoup
import requests

url = requests.get('https://realpython.com/atom.xml')

soup = BeautifulSoup(url.content, 'xml')
entries = soup.find_all('entry')

for entry in entries:
  title = entry.title.text
  summary = entry.summary.text
  link = entry.link['href']
  print(f"Title: {title}\nSummary: {summary}\nLink: {link}\n---------------")