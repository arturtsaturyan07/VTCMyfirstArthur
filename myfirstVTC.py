import math
angle = int(input())
x_coord = math.cos
y_coord = math.sin
special_angles = [(math.radians(0), '1', '0', '0', '0'), (math.radians(30), '√3/2', '1/2', ' π/6', 'π/3'), (math.radians(45), '√2/2', '√2/2', ' π/4', 'π/4'), (math.radians(60), '1/2', '√3/2', ' π/3', ' π/6'), (math.radians(90), '0', '1', ' π/2', '2π'), (math.radians(180), '-1', '0', ' π',  ' π/2'), (math.radians(150), '-√3/2', '1/2', '5*π/6', '2*π/3'), (math.radians(135), '-√2/2', '√2/2', '3*π/4', '3*π/4'), (math.radians(120), '-1/2', '√3/2', '2*π/3', '5*π/6'), (math.radians(270), '0', '-1','/2π', '3*π/2'), (-math.radians(30), '-√3/2', '1/2', '2*π/3', '5*π/6')]
while not (0 <= abs(angle) <= 180):
    if 180 <= angle <= 360:
        angle -= 180
        angle = -angle
    elif angle > 360:
        x = angle // 360
        angle -= x * 360

for a, c, s, a_c, a_s in special_angles:
    if math.radians(angle) == a:
        print(angle)
        if abs(a) == a:
            print(f'X_coord is {x_coord(a)}, for cosinus angle is {a_c}, Y_coord is {y_coord(a)}, for sinus angle is {a_s}')
        else:
            print(f'X_coord is {-x_coord(a)}, for cosinus angle is {a_c}, Y_coord is {y_coord(a)}, for sinus angle is {a_s}')