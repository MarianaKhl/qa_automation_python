import requests

# server URL
base_url = 'http://127.0.0.1:8080'


def upload_image(image_path):
    upload_url = f'{base_url}/upload'

    # send a POST request to download the image
    with open(image_path, 'rb') as img:
        files = {'image': img}
        response = requests.post(upload_url, files=files)

    if response.status_code == 201:
        print("Image uploaded successfully!")
        json_response = response.json()
        image_url = json_response['image_url']
        print(f"Image URL: {image_url}")
        return image_url
    else:
        print(f"Error loading image: {response.status_code}")
        print(response.text)
        return None


def get_image(image_name, content_type="text"):
    get_image_url = f'{base_url}/image/{image_name}'

    # 'Accept' for GET request
    headers = {'Accept': 'application/json'} if content_type == "text" else {'Accept': 'image/*'}

    response = requests.get(get_image_url, headers=headers)

    if response.status_code == 200:
        if content_type == "text":
            json_response = response.json()
            image_url = json_response['image_url']
            print(f"Image URL: {image_url}")
        elif content_type.startswith("image"):
            with open(f'downloaded_{image_name}', 'wb') as f:
                f.write(response.content)
            print(f"Image saved as downloaded_{image_name}")
    else:
        print(f"An error occurred while receiving the image: {response.status_code}")
        print(response.text)


def delete_image(image_name):
    delete_url = f'{base_url}/delete/{image_name}'

    response = requests.delete(delete_url)

    if response.status_code == 200:
        print("Image deleted successfully!")
    else:
        print(f"Error deleting image: {response.status_code}")
        print(response.text)


if __name__ == '__main__':
    # 1. check download image
    image_path = '/Users/marianna/PycharmProjects/demo/Lesson_2-GitHub-/lesson_19/mars_photo1.jpg'
    uploaded_image_url = upload_image(image_path)

    if uploaded_image_url:
        # 2. check get image
        image_name = uploaded_image_url.split('/')[-1]  # get the name of the image from the URL
        get_image(image_name, content_type="text")

        get_image(image_name, content_type="image/jpeg")

        # 3. check delete image
        delete_image(image_name)

