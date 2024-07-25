import requests
import click

DEFAULT_QUOTE = 'Could not retrieve quote.'
DEFAULT_IMAGE_TEXT = "Could not retrieve image."

def get_data(key=''):
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
        image_url = requests.get('https://picsum.photos/300/300').url
    except requests.exceptions.RequestException:
        image_url = None

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
    if data["image_url"]:
        click.echo(f'Image URL: {data["image_url"]}')
    else:
        click.echo(click.style(DEFAULT_IMAGE_TEXT, fg='red'))

if __name__ == '__main__':
    cli()
