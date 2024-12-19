from google_images_search import GoogleImagesSearch

# Provide your API key and CX
gis = GoogleImagesSearch('AIzaSyD6Zfamdisx21aHKLO6CAiu112YlsGCdlY', 'a1975c22331d346f8')

# Search parameters without specifying 'imgSize'
_search_params = {
    'q': 'grayscale texture',  # Query string
    'num': 20,                 # Number of images to fetch
    'safe': 'off',             # Disable safe search
    'fileType': 'jpg'          # Fetch only JPEG images
}

# Perform the search
gis.search(search_params=_search_params, path_to_dir='downloads')

# Print confirmation
print("Images downloaded to: downloads")
