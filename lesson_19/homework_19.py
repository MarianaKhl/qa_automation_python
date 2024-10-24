import requests
import os

# the URL to request
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

# query parameters
params = {
    'sol': 1000,  # day of rover work on Mars
    'camera': 'fhaz',  # camera from which the photo was taken (Front Hazard Avoidance Camera)
    'api_key': 'DEMO_KEY'  # API keyv = 'DEMO_KEY'
}

# make a request to the NASA API
response = requests.get(url, params=params)

# check whether the request was successful
if response.status_code == 200:
    data = response.json()  #  receive JSON data
    photos = data.get('photos', [])  # get a list of photos

    # check if there is a photo
    if not photos:
        print("There are no photos for these parameters")
    else:
        # download the first few photos (for example, 5)
        for idx, photo in enumerate(photos[:5], start=1):
            img_url = photo['img_src']  # get URL to photo
            print(f"Download the photo {idx}: {img_url}")

            # making a request to receive a photo
            img_data = requests.get(img_url).content

            # create the file name
            file_name = f"mars_photo{idx}.jpg"

            # save the photo locally
            with open(file_name, 'wb') as file:
                file.write(img_data)

            print(f"Photo save as: {file_name}")

else:
    print(f"API request error: {response.status_code}")
