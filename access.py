import requests
import json
import config

clientid = config.imgur_client_id # Imgur client token 
base_album_url = "https://api.imgur.com/3/album/" # Base URL


def randomImage(command): # Grabs the album id based on the command being used
    if command == "hug":
        album_id = "dZQCkGv"
    if command == "ai":
        album_id = "wTBWPJw"
    
    # Generate a URL with the given arguements and parse the JSON file from the URL
    url = base_album_url + album_id + "?client_id=" + clientid
    req = requests.get(url)
    data = req.text
    parsed_data = json.loads(data)

    parsed_data = parsed_data["data"]
    images = parsed_data["images"]
    image_urls = [i["link"]for i in images] # Put all the image links into an array
    return image_urls # Return the array back to the bot command being used







