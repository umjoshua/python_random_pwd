#add pyqrcode and pypng modules via terminal
#python -m pip install pyqrcode
#python -m pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

link=input("Enter link: ")

url=pyqrcode.create(link)
url.png('qr.png',scale=6)
