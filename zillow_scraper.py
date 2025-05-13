import requests
from bs4 import BeautifulSoup
from datetime import datetime

SENDGRID_API_KEY = "your_api_key_here"
TO_EMAIL = "you@example.com"
FROM_EMAIL = "you@example.com"
ZIP_CODES = ["30058"]
HEADERS = {"User-Agent": "Mozilla/5.0"}

def generate_urls():
    return [f"https://www.zillow.com/homes/fsbo/{zip_code}_rb/" for zip_code in ZIP_CODES]

def scrape_zillow(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    listings = soup.select("article")
    results = []
    for listing in listings:
        link = listing.find("a", href=True)
        price = listing.find("span", {"data-test": "property-card-price"})
        address = listing.find("address")
        if link and price and address:
            results.append({
                "link": "https://www.zillow.com" + link["href"],
                "price": price.get_text(strip=True),
                "address": address.get_text(strip=True),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return results
