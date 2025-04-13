import httpx
from selectolax.parser import HTMLParser


def get_html(baseurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    resp = httpx.get(baseurl, headers=headers)
    html = HTMLParser(resp.text)
    return html


def extract_text(html, sel):
    try:
        return html.css_first(sel).text().strip()  # .replace("\xa0", "")
    except AttributeError:
        return None


def parse_page(html):
    products = html.css("div.product-block")

    for product in products:
        # price = product.css_first('.b-product-gallery__current-price')
        # cleaned_price = price.replace('\xa0', '')
        item = {
            "name": extract_text(product, "a.product-block-name-link"),
            "price": extract_text(product, "span.product-price.is-avalible"),
            # "old price": extract_text(product, ".b-product-gallery__old-price"),
        }
        print(item)


def main():
    baseurl = "https://qwertyshop.ua/noutbuki-apple-macbook-pro/sort=expensive"
    html = get_html(baseurl=baseurl)
    parse_page(html)


if __name__ == "__main__":
    main()
