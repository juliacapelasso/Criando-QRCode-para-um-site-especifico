#QR code usando Python

#Importar a biblioteca
import pyqrcode 
import png

from pyqrcode import QRCode

#Escolher o site que você quer que o QRCode direcione
s = 'https://github.com/juliacapelasso'

#Fazer o Python criar o QRCode a partir do link desejado
url = pyqrcode.create(s)

#Fazer o Python abrir uma janela mostrando seu QRCode pronto
pyqrcode.QRCode.show(url)




