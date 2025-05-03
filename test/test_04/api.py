# https://youtu.be/cyURNr9LZdM?si=t4HSsnfT8m83eCGA

import requests


def main():
    print("Search the Art institute")
    artist = input("Specify artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist})
        # To verify if I got http 200 OK ?
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    print(response)
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
