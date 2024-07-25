from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

def getData(key=''):
    quote_url = f'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
    if key:
        quote_url += f'&key={key}'
    quote_response = requests.get(quote_url)
    data = quote_response.json()
    quote = data.get('quoteText', 'No quote available')
    quote_author = data.get('quoteAuthor', 'Unknown')
    quote_string = f'"{quote}" - {quote_author}'
    image_url = requests.get('https://picsum.photos/300/300').url
    print(quote_url)
    return {"quote": quote_string, "image_url": image_url}

@app.route('/')
def index():
    key = request.args.get('key', '')
    data = getData(key)
    return render_template('index.html', quote=data['quote'], image_url=data['image_url'])

@app.route('/refresh', methods=['GET'])
def refresh():
    key = request.args.get('key', '')
    data = getData(key)
    return jsonify({'quote': data['quote'], 'image_url': data['image_url']})

if __name__ == '__main__':
    app.run(debug=True)
