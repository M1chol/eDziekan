from html2image import Html2Image
from PIL import Image

hti = Html2Image(browser='edge')
hti.screenshot(
    html_file='response.html',
    size=(540,560),
    save_as='table.png'
)
img = Image.open('table.png')
img = img.crop((156,123,540,560))
img.save('final.png')