# ── v1_search.py ──────────────────────────────────────────────
# First iteration of the museum search — single file, no packages
# Searches artworks only, no error message on failure

import requests

def main():
    print("Search the Art Institute of Chicago")
    artist = input("Artist: ")
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
        print(f"* {artwork['title']}")

main()