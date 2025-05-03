from artwork import get_artworks
from artists import get_artists


def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=5)
    artists = get_artists(query=artists, limit=5)
    for artwork in artworks:
        print(f"* {artwork}")


main()
