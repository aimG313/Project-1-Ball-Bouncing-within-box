import vpython as vp


t = 0.2 # wall thickess
l = 15 #length
w = 20 #width
h = 10 #height
r = 1 #ball radius

floor = vp.box(pos = vp.vector(0,-h/2,0),color = vp.color.white, size = vp.vector(l,t,w))
ceiling = vp.box(pos = vp.vector(0,h/2,0),color = vp.color.white, size = vp.vector(l,t,w))
right_wall = vp.box(pos = vp.vector(l/2,0,0),color = vp.color.white, size = vp.vector(t,h+t,w))
left_wall = vp.box(pos = vp.vector(-l/2,0,0),color = vp.color.white,size = vp.vector(t,h+t,w))
back_wall = vp.box(pos = vp.vector(0,0,w/2),color = vp.color.white, size = vp.vector(l+t,h+t,t))
ball = vp.sphere(pos = vp.vector(0,0,0),color = vp.color.red,radius = r)

x_pos = 0
y_pos = 0
z_pos = 0

delta_x = 0.1
delta_y = 0.1
delta_z = 0.1

while True:
  vp.rate(50)
  
  x_pos += delta_x
  y_pos += delta_y
  z_pos += delta_z
  
  
  if x_pos > l/2-r or x_pos < -(l/2-r):
    delta_x = -delta_x
    
  if y_pos > h/2-r or y_pos < -(h/2-r):
    delta_y = -delta_y
    
  if z_pos > w/2-r or z_pos < -(w/2-r):
    delta_z = -delta_z
    
  ball.pos = vp.vector(x_pos,y_pos,z_pos)
  
  