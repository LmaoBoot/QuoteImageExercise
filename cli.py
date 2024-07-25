import requests
import click

def get_data(key=''):
    quote_url = f'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
    if key:
        quote_url += f'&key={key}'
    quote_response = requests.get(quote_url)
    data = quote_response.json()
    quote = data.get('quoteText', 'No quote available')
    quote_author = data.get('quoteAuthor', 'Unknown')
    quote_string = f'"{quote}" - {quote_author}'
    image_url = requests.get('https://picsum.photos/300/300').url
    return {"quote": quote_string, "image_url": image_url}

@click.command()
@click.option('--key', default='', help='Optional key for the quote API (integer, max 6 digits).')
def cli(key):
    if key and not key.isdigit():
        click.echo('Key must be an integer.')
        return
    if len(key) > 6:
        click.echo('Key must be at most 6 digits long.')
        return

    data = get_data(key)
    click.echo(f'Quote: {data["quote"]}')
    click.echo(f'Image URL: {data["image_url"]}')

if __name__ == '__main__':
    cli()
