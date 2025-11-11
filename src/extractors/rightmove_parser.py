thonimport requests
from bs4 import BeautifulSoup

def parse_rightmove(url):
    """
    Function to extract property data from a Rightmove listing.
    """
    # Send a GET request to the property URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract required data
    property_data = {
        'url': url,
        'address': soup.find('h1', {'class': 'property-heading'}).get_text(strip=True),
        'price': soup.find('span', {'class': 'property-price'}).get_text(strip=True),
        'description': soup.find('div', {'class': 'description'}).get_text(strip=True),
        'beds': int(soup.find('span', {'class': 'bedrooms'}).get_text(strip=True).split()[0]),
        'baths': int(soup.find('span', {'class': 'bathrooms'}).get_text(strip=True).split()[0]),
        'images': [img['src'] for img in soup.find_all('img', {'class': 'property-image'})],
        'features': [feature.get_text(strip=True) for feature in soup.find_all('li', {'class': 'property-feature'})],
    }
    
    return property_data