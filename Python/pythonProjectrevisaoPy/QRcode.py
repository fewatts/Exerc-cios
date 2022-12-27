import qrcode

Image = qrcode.make(
    'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
)
Image.save('MYQRCODE.png')
Image.show()
