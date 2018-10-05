import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.g9.co.kr')

html = req.text
soup = BeautifulSoup(html, 'html.parser');

g9_images = soup.select('.img-bannercard')

# with open('g9_images', 'w') as f:
#     for image in g9_images:
#         print(image.get('alt') + ' : ' + image.get('src'))
#         f.write(image.get('alt') + ' : ' + image.get('src') + '\n')
# f.closed

def image_save(imageTag):
    image_url = imageTag.get('src');
    image_extension = image_url.split(".")[-1]
    image_name = imageTag.get('alt') + '.' + image_extension
    print(image_name)

    image_request = requests.get(image_url)

    with open(image_name, "wb") as code:
        code.write(image_request.content)
    code.close()

for image in g9_images:
    image_save(image)
