import os
import cv2
import numpy
import glob

from selenium import webdriver
from PIL import Image

def screenshot(arr):
    i = arr[0]
    j = arr[2]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=256x256")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome("../chromedriver", chrome_options=chrome_options)
#    driver = webdriver.Chrome("./chromedriver")
    return None
    k = 0
    l = 0

    while(j < arr[3] + 1):
        i = arr[0]
        while(i < arr[1] + 1):    
            url = 'https://gris.gg.go.kr:8888/grisgis/rest/services/bdsMap_Cbnd_Cache/MapServer/tile/10/%s/%s' % (str(j), str(i))
            driver.get(url)
            filename = 'images/10/%s_%s.png' % (str(j), str(i))
            driver.save_screenshot(filename)
            print("save %s_%s.png" % (str(j), str(i)))

            i = i + 1
            k = k + 1
        j = j + 1
        l = l + 1


def append_images(arr):
    i = arr[0]
    j = arr[2]
    k = 0
    l = 0

    pixel_x = (arr[1] - arr[0] + 1) * 256
    pixel_y = (arr[3] - arr[2] + 1) * 256

    result = Image.new("RGBA", (pixel_x, pixel_y))


    while(j < arr[3] + 1):
        i = arr[0]
        k = 0
        while(i < arr[1] + 1):
            filename = 'images/10/%s_%s.png' % (str(j), str(i))
            print('j = %s, i = %s' % (str(j), str(i)))
            im = Image.open(filename)
            result.paste(im=im, box=(k * 256, l * 256))
            i = i + 1
            k = k + 1
        j = j + 1
        l = l + 1

    result.save('result.png')    


def append_with_opencv(arr):
    i = arr[0]
    j = arr[2]
    k = 0
    l = 0

    dir = "."
    ext = ".pdf"

    pathname = os.path.join(dir, "*" + ext)
    images = [cv2.imread(img) for img in glob.glob("images")]
    height = 35840
    width = 30208
    output = numpy.zeros((height, width, 3))
    y = 0
    x = 0
    for image in images:
        h, w, d = image.shape
        output[y:y + h, x : x+w] = image
        print("x = %s, y = %s" % (str(x), str(y)))
        if x == arr[1] - arr[0]:
            x = 0
            y = y + 1

    cv2.imwrite("result.pdf", output)


def start():
#    x_min = 138734
#    x_max = 138851
#    y_min = 143841
#    y_max = 143980

    x_min = 69375
    x_max = 69404
    y_min = 71925
    y_max = 71972
    
    arr = [x_min, x_max, y_min, y_max]
    screenshot(arr)
#    append_images(arr)
#    append_with_opencv(arr)

if __name__ == "__main__":
    start()
