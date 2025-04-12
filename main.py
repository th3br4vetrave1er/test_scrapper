import httpx
from selectolax.parser import HTMLParser


url = 'https://td.zp.ua/ua/g137334460-kompyuteri-zbirki'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)


def extract_text(html, sel):
    try:
        return html.css_first(sel).text().replace('\xa0', '')
    except AttributeError:
        return None


products = html.css('li.b-product-gallery__item')


for product in products:
    # price = product.css_first('.b-product-gallery__current-price')
    # cleaned_price = price.replace('\xa0', '')
    item = {
        'name': extract_text(product, '.b-product-gallery__title'),
        'price': extract_text(product, '.b-product-gallery__current-price')
    }
    print(item)


def main():
    print("Hello from test-scrapper!")


if __name__ == "__main__":
    main()
