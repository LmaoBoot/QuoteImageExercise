from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

DEFAULT_QUOTE = '"The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt'
DEFAULT_IMAGE_TEXT = "Could not retrieve image."

def get_data(key='', grayscale=False):
    try:
        quote_url = f'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
        if key:
            quote_url += f'&key={key}'
        quote_response = requests.get(quote_url)
        data = quote_response.json()
        quote = data.get('quoteText', 'No quote available')
        quote_author = data.get('quoteAuthor', 'Unknown')
        quote_string = f'"{quote}" - {quote_author}'
    except (requests.exceptions.RequestException, ValueError, KeyError):
        quote_string = DEFAULT_QUOTE

    try:
        image_url = 'https://picsum.photos/300/300'
        if grayscale:
            image_url += '?grayscale'
        print(grayscale)
        image_url = requests.get(image_url).url
    except requests.exceptions.RequestException:
        image_url = None

    
    return {"quote": quote_string, "image_url": image_url}

@app.route('/')
def index():
    key = request.args.get('key', '')
    data = get_data(key)
    return render_template('index.html', quote=data['quote'], image_url=data['image_url'])

@app.route('/refresh', methods=['GET'])
def refresh():
    key = request.args.get('key', '')
    grayscale = request.args.get('grayscale', 'false') == 'true'
    data = get_data(key, grayscale)
    return jsonify({'quote': data['quote'], 'image_url': data['image_url']})

if __name__ == '__main__':
    app.run(debug=True)
