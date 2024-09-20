#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# URL of News Site
url = "https://www.bbc.com/news"
html_file_name = 'news_html.html'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
print(response.status_code)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    with open(html_file_name,'w', encoding="utf-8") as html_db: 
        html = soup.prettify()
        html_db.write(html)
