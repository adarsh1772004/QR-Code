import image 
import qrcode
myqr=qrcode.QRCode(version=15, box_size=10, border=5)
data="Adarsh"
myqr.add_data(data)
myqr.make(fit=True)
img=myqr.make_image(fill="black", back_color="white")
img.save("myqr.png")