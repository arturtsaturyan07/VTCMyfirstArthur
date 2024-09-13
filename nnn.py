import math

initial_angle = int(input('Ներմուծեք պտտման անկյունը։ '))


def trigonometry(initial_angle):
    rad = (initial_angle * math.pi) / 180
    angle = 0
    if -360 < initial_angle < 0:
        angle = initial_angle % 360
        if angle <= 0:
            angle += 360
        angle = angle % 90
        print(
            f'cos({initial_angle})=-cos({angle})={math.cos(initial_angle)} \nsin({initial_angle})=-sin({angle})={math.sin(initial_angle)}')
    elif 360 < initial_angle:
        x = initial_angle // 360
        angle = initial_angle - 360 * x
        rad = (angle * math.pi) / 180
        print(
            f'{initial_angle} և {angle} անկյունների եռանկյունաչափական ֆունկցիաների արժեքները կարող ենք կապել հետևյալ կերպ՝')
        print(
            f'cos({initial_angle})=cos({initial_angle}-360*{x})=cos({angle})={math.cos(rad)} \nsin({initial_angle})=sin({initial_angle}-360*{x})=sin({angle})={math.sin(rad)}' if abs(
                angle) != 180 and angle != 90 and angle != 270 else f'cos({initial_angle})=cos({initial_angle}-360*{abs(x)})=cos({angle})=-1 \nsin({initial_angle})=sin({initial_angle}-360*{abs(x)})=sin({angle})=0' if angle != 90 else f'cos({initial_angle})=cos({initial_angle}+360*{abs(x)})=cos({angle})=0 \nsin({initial_angle})=sin({initial_angle}+360*{abs(x)})=sin({angle})=1' if angle != 270 else f'cos({initial_angle})=cos({initial_angle}+360*{abs(x)})=cos({angle})=0 \nsin({initial_angle})=sin({initial_angle}+360*{abs(x)})=sin({angle})=-1')
    elif -360 > initial_angle:
        x = abs(initial_angle // 360)
        angle = initial_angle + abs(360 * x)
        rad = (angle * math.pi) / 180
        print(
            f'{initial_angle} և {angle} անկյունների եռանկյունաչափական ֆունկցիաների արժեքները կարող ենք կապել հետևյալ կերպ՝')
        print(
            f'cos({initial_angle})=cos({initial_angle}-360*{x})=cos({angle})={math.cos(rad)} \nsin({initial_angle})=sin({initial_angle}-360*{x})=sin({angle})={math.sin(rad)}' if abs(
                angle) != 180 and angle != 90 and angle != 270 else f'cos({initial_angle})=cos({initial_angle}-360*{abs(x)})=cos({angle})=-1 \nsin({initial_angle})=sin({initial_angle}-360*{abs(x)})=sin({angle})=0' if angle != 90 else f'cos({initial_angle})=cos({initial_angle}+360*{abs(x)})=cos({angle})=0 \nsin({initial_angle})=sin({initial_angle}+360*{abs(x)})=sin({angle})=1' if angle != 270 else f'cos({initial_angle})=cos({initial_angle}+360*{abs(x)})=cos({angle})=0 \nsin({initial_angle})=sin({initial_angle}+360*{abs(x)})=sin({angle})=-1')
    elif 0 < initial_angle < 90:
        print(f'cos({initial_angle})={math.cos(math.radians(initial_angle))} \nsin({initial_angle})={math.sin(rad)}')
    elif 90 < initial_angle < 180:
        print(
            f'cos({initial_angle})=cos(180-{180 - initial_angle})=-cos({180 - initial_angle})={math.cos(rad)} \nsin({initial_angle})=sin(180-{180 - initial_angle})=sin({180 - initial_angle})={math.sin(rad)}')
    elif 180 < initial_angle < 270:
        print(
            f'cos({initial_angle})=cos(180+{initial_angle - 180})=-cos({initial_angle - 180})={math.cos(rad)} \nsin({initial_angle})=sin(180+{initial_angle - 180})=-sin({initial_angle - 180})={math.sin(rad)}')
    elif 270 < initial_angle < 360:
        print(
            f'cos({initial_angle})=cos(360-{360 - initial_angle})=cos({360 - abs(initial_angle)})={math.cos(rad)} \nsin({initial_angle})=sin(360-{360 - initial_angle})=-sin({360 - abs(initial_angle)}))={math.sin(rad)}')
    elif initial_angle == 90:
        print(f'cos(90)=0 \nsin(90)=1')
    elif initial_angle == 180:
        print(f'cos(180)=-1 \nsin(180)=0')
    elif initial_angle == 270:
        print(f'cos(270)=0 \nsin(270)=-1')
    elif initial_angle == 0:
        print(f'cos(0)=1 \nsin(0)=0')


trigonometry(initial_angle)
