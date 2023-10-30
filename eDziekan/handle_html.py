from html2image import Html2Image
from PIL import Image
from handle_requests import target_name

temp_img_name = 'temp.png'
target_img_name = 'final.png'

def convert():
    print("Converting to img using Edge...")
    hti = Html2Image(browser='edge')
    hti.screenshot(
        html_file=target_name,
        save_as=temp_img_name
    )
    img = Image.open(temp_img_name)
    # img = img.crop((156,123,700,440))
    img.save(target_img_name)