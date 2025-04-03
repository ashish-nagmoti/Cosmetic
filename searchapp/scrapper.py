import requests
from bs4 import BeautifulSoup

# A common header to simulate a browser request.
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/115.0 Safari/537.36")
}

def scrape_nykaa(query):
    search_url = f"https://www.nykaa.com/search/result/?q={query}"
    response = requests.get(search_url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product details
        products = []
        product_containers = soup.select('div.productWrapper.css-17nge1h')  

        for product in product_containers:
            try:
                name = product.select_one('div.css-xrzmfa').get_text(strip=True)  # Get Product Name
                price = product.select_one('div.css-1d0jf8e span span').get_text(strip=True)  # Get Price
                link = product.select_one('a.css-qlopj4')['href']  # Get Product Link
                image = product.select_one('img.css-11gn9r6')['src']  # Get Image URL

                # Ensure full URL for the product link
                full_link = f"https://www.nykaa.com{link}" if link.startswith("/") else link

                products.append({
                    'name': name,
                    'price': price,
                    'link': full_link,
                    'image': image
                })
            except Exception:
                continue

        return products
    else:
        print("Error fetching search results")
        return []


def scrape_amazon(query):
    products = []
    url = f"https://www.amazon.in/s?k={query}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        

        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        product_containers = soup.select("div.s-result-item[data-asin]")
        
        for product in product_containers:
            try:
                title_tag = soup.select_one("h2.a-size-base-plus span")
                name= title_tag.text.strip() if title_tag else "N/A"
                
                price_tag = soup.select_one("span.a-price > span.a-offscreen")
                price = price_tag.text.strip() if price_tag else "N/A"
                
                a_tag = soup.find('a', class_='a-link-normal s-no-outline')
                if a_tag and 'href' in a_tag.attrs:
                    product_link = a_tag['href']
    
                # If found, format the complete Amazon URL
                if product_link:
                    link = "https://www.amazon.com/" + product_link.split('&url=')[-1]
    
    

                
                image_tag = soup.select_one("img.s-image")
                image= image_tag['src'] if image_tag else "N/A"
                
                products.append({
                    'name': name,
                    'price': price,
                    'link': link,
                    'image': image
                })
            except Exception:
                continue
        print(products)  
        return products
    else:
        print("Error fetching search results")
        return []

def scrape_tira(request):
    pass
