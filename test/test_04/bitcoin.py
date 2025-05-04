import sys
import requests


def main():
    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?api"
                         "Key=6780f5c81638527395262cc08ccdf2c08d95f07e68d14af794fa420f5071823b")
        r.raise_for_status()
    except requests.HTTPError \
           and requests.ConnectionError \
           and requests.TooManyRedirects \
           and requests.ConnectTimeout \
           and requests.ReadTimeout \
           and requests.Timeout:
        sys.exit("Error happened ")

    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Error happened. Specify a number ")

    content = r.json()
    price_usd = float(content["data"]["priceUsd"])
    price = price_usd * float(sys.argv[1])
    print(f"${price:,.4f}")


if __name__ == '__main__':
    main()
