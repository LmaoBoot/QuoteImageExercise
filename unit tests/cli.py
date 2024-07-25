import requests
import click

DEFAULT_QUOTE = '"The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt'
DEFAULT_IMAGE_TEXT = "Could not retrieve image."

def get_data(key='', grayscale=False):
    # For testing purposes, we'll use fixed values
    quote_string = DEFAULT_QUOTE
    image_url = None

    if grayscale:
        image_url = 'http://testimage.com/test.jpg'
    
    return {"quote": quote_string, "image_url": image_url}

@click.command()
@click.option('--key', default='', help='Optional key for the quote API (integer, max 6 digits).')
@click.option('--grayscale', is_flag=True, help='Toggle grayscale for the image.')
def cli(key, grayscale):
    if key and not key.isdigit():
        click.echo('Key must be an integer.')
        return
    if len(key) > 6:
        click.echo('Key must be at most 6 digits long.')
        return

    data = get_data(key, grayscale)
    click.echo(f'Quote: {data["quote"]}')
    if data["image_url"]:
        click.echo(f'Image URL: {data["image_url"]}')
    else:
        click.echo(click.style(DEFAULT_IMAGE_TEXT, fg='red'))

if __name__ == '__main__':
    cli()
