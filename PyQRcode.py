import pyqrcode
data='vikaskumargond.ml'
img=pyqrcode.create(data)
img.png('porfoliowebsite.png',scale=10)