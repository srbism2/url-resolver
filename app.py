from flask import Flask
import requests
from flask_cors import CORS
from flask import request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    url = request.args.get('url')
    url1 = requests.get(url).url
    return jsonify(url1)

@app.route('/flipkart_info/')
def flip_info():
    url = request.args.get('url')
    flipkart_response = hit_url(flipkart_url)
    price = get_flipkart_price(flipkart_response)
    image = get_flipkart_image(flipkart_response)
    
    # Display the fetched data
    flipkart_json = {"image" : image, "price" : price}
    return jsonify(flipkart_json)
    
def get_flipkart_price(response):
    try:
        response = response
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            price = soup.find('div', {'class': '_30jeq3 _16Jk6d'}).text.strip()
            return price
        else:
            print("Failed to retrieve price from Flipkart. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_flipkart_image(response):
    try:
        response = response
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            image_tag = soup.find('img', {'class': '_396cs4 _2amPTt _3qGmMb'})
            if image_tag:
                image_url = image_tag['src']
                return image_url
            else:
                print("Image not found on Flipkart.")
                return None
        else:
            print("Failed to retrieve image from Flipkart. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None  
def hit_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        else:
            return None 
    except Exception as e:
        print("An error occurred:", str(e))
        return None 


if __name__ == '__main__':
    app.run()
