import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def fetch_reviews(self, url):
        try:
            # Step 1: Clean the URL to ensure it's the desktop review page
            url = url.replace("m.snapdeal.com", "www.snapdeal.com").split('#')[0]
            if "/reviews" not in url:
                url = url.split('?')[0] + "/reviews"

            print(f"Connecting to: {url}")
            response = requests.get(url, headers=self.headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            reviews = []
            
            # Step 2: Try multiple possible review containers
            review_blocks = soup.select('.user-review') or soup.select('.commentlist') or soup.select('.review-section')

            for item in review_blocks:
                # Extracting text - looks for 'p' tags or common review body classes
                text_elem = item.find('p') or item.select_one('.user-review--copy')
                
                # Extracting author and metadata [cite: 10]
                author_elem = item.select_one('.user-name') or item.find('span', class_='user-name')
                date_elem = item.select_one('.review-date')
                
                if text_elem and len(text_elem.text.strip()) > 5:
                    reviews.append({
                        "author": author_elem.text.strip() if author_elem else "Snapdeal Customer",
                        "date": date_elem.text.strip() if date_elem else "Recent",
                        "rating": "5", # Default rating [cite: 10]
                        "text": text_elem.text.strip().replace("READ MORE", "")
                    })
            
            print(f"Successfully extracted {len(reviews)} reviews.")
            return reviews
            
        except Exception as e:
            print(f"Scraping Error: {e}") [cite: 14]
            return []