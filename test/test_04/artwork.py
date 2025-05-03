import requests


def get_artworks(query, limit):

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": query, "limit": limit})
        # To verify if I got http 200 OK ?
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return


