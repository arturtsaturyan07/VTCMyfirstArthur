from PIL import Image

im = Image.open("korea.jpg")
pixels = im.load() # պիքսելներ պարունակող ցուցակ
x, y = im.size # պատկերի լայնությունը (x) և բարձրությունը (y)

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = g, b, r

im.save("Ռիանա2.jpg")