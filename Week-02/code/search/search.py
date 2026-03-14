"""
import requests

def main():
    print("Search the Art Institute of Chicago")
    artist = input("Arist: ")
    try:
        responce = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
            )
        responce.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete requests")
    content = responce.json()
    for artwork in content["data"]:
        print(f"* {artwork ['title']}")

main()
"""
from museum.artists import get_artists
from museum.artwork import get_artworks
def main():
    print("If you want to search by Artist input 1")
    print("If you want to search by Artwork input 2")
    search_type = int(input("What do you want to search by: "))
    if search_type == 1:
        artist = input("Artist:")
        artists = get_artists(query= artist, limit=3)
        for artist in artists:
            print(f"* {artist}")
    elif search_type == 2:
        artwork = input("Artwork:")
        artworks = get_artworks(query= artwork, limit=3)
        for artwork in artworks:
            print(f"* {artwork}")
    else:
        print("Please input the correct search type")
        return
main()
