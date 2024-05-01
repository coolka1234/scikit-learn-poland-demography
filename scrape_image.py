import requests

def download_image(img_url, filename):
    response = requests.get(img_url, stream=True)

    if response.status_code == 200:
        with open(filename, 'wb') as out_file:
            out_file.write(response.content)
        print(f"Downloaded image successfully - {filename}")
    else:
        print(f"Unable to download image. HTTP response code - {response.status_code}")

img_url = "https://static.zpe.gov.pl/portal/f/res-minimized/R1DRpEwOu0kly/4/fYPhB0sYKSWe5DLdlULEQRUZjaP4NGsL.png"
filename = "urbanizacjawPolsce.png"

download_image(img_url, filename)