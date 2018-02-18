import urllib.request
import random

def download_image(url):
    name=random.randrange(1,200)
    fname=str(name)+'.jpg'
    urllib.request.urlretrieve(url,fname)

download_image("http://www.keenthemes.com/preview/conquer/assets/plugins/jcrop/demos/demo_files/image1.jpg")