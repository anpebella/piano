window_width=800
window_height=600

white=(255,255,255)
black=(0,0,0)
grey=(20,20,20)
act_color=(0,0,0)
but_width=80
but_height=150
start_x=100
start_y=120

keys={'a':'assets/sounds/a6.mp3',
      'b':'assets/sounds/b6.mp3',
      'c':'assets/sounds/c6.mp3',
      'd':'assets/sounds/d6.mp3',
      'e':'assets/sounds/e6.mp3',
      'f':'assets/sounds/f6.mp3',

      'g':'assets/sounds/g6.mp3'}

text=['press A','press B','press C','press D','press E','press F','press G']
fonte=font.Font(None,20)

img=[transform.scale(image.load('assets/images/a.jpg'), (80, 150)),
transform.scale(image.load('assets/images/b.jpg'), (80, 150)),
transform.scale(image.load('assets/images/c.jpg'), (80, 150)),
transform.scale(image.load('assets/images/d.jpg'), (80, 150)),
transform.scale(image.load('assets/images/e.jpg'), (80, 150)),
transform.scale(image.load('assets/images/f.jpg'), (80, 150)),
transform.scale(image.load('assets/images/g.jpg'), (80, 150))]

hover=[transform.scale(image.load('assets/images/a1.jpg'),(80,150)),
transform.scale(image.load('assets/images/b1.jpg'),(80,150)),
transform.scale(image.load('assets/images/c1.jpg'),(80,150)),
transform.scale(image.load('assets/images/d1.jpg'),(80,150)),
transform.scale(image.load('assets/images/e1.jpg'), (80, 150)),
transform.scale(image.load('assets/images/f1.jpg'), (80, 150)),
transform.scale(image.load('assets/images/g1.jpg'), (80, 150))]

set_img=transform.scale(image.load('assets/images/set.png'),(50,50))
set_hover=transform.scale(image.load('assets/images/set1.png'),(50,50))
