import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = 'https://indianexpress.com/'
    
    try:
        # Send a GET request to the website
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return

        # Parse the webpage content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article elements
        articles = soup.find_all('h3')

        if not articles:
            print("No articles found on the page.")
            return

        # Extract and print the titles and links
        for article in articles:
            title = article.text.strip()
            link = article.find('a')
            if link and 'href' in link.attrs:
                full_link = f"https://www.bbc.com{link['href']}"
                print(f'Title: {title}')
                print(f'Link: {full_link}')
                print('---')
            else:
                print(f"Skipping an article due to missing link: {title}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the web scraper
scrape_news()
