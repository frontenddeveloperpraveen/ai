import requests
import sys
from PIL import Image
from PIL import Image, ImageOps, ImageFilter
try:
    def sketch():
        image = Image.open('APP/static/1.png')
        image = image.convert('L')
        image = ImageOps.invert(image)
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
        image.save('APP/static/1.png')
    def Gen(prompt):
        API_KEY = '' #Your API KEY
        URL = 'https://api.pexels.com/v1/search'
        params = {
            'query': prompt,
            'per_page': 4,
        }
        headers = {
            'Authorization': API_KEY,
        }
        def think():
            response = requests.get(URL, params=params, headers=headers)
            image_url = response.json()['photos'][0]['src']['large']
            image_data = requests.get(image_url).content
            try:
                with open('APP/static/1.png', 'wb') as f:
                    f.write(image_data)
            except IndexError:
                print("IMAGE ERROR")
                Gen()
            try:
                img = Image.open('APP/static/1.png')
            except KeyboardInterrupt:
                sys.stdout.write("\rLoading canceled.  \n")
        think()
        #sketch()
except IndexError :
    print("No Image Found - I'm Sorry")
