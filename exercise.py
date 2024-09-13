from PIL import Image, ImageDraw


def folio(w, book='#c99d3b', cover='#963', bookmark='#be72b1', star='#ff0', border='#ffc000', spiral='#663828'):
    im = Image.new('RGB', (24 * w, 20 * w), color='white')
    dr = ImageDraw.Draw(im)
    dr.ellipse(((10 * w, 2 * w), (14 * w, 4 * w)), cover)
    dr.ellipse(((10.25 * w, 2.25 * w), (13.75 * w, 3.75 * w)), book)
    dr.rectangle(((w, 3 * w), (23 * w, 17 * w)), cover)
    dr.rectangle((((1.25 * w, 3.25 * w), (22.75 * w, 16.75 * w))), book)
    dr.polygon(((11.5 * w, 3 * w), (11.5 * w, 18 * w), (11 * w, 19 * w), (13 * w, 19 * w), (12.5 * w, 18 * w),
                (12.5 * w, 3 * w)), bookmark)
    dr.polygon(((18 * w, 4.75 * w), (17 * w, 9 * w), (14.75 * w, 10 * w), (17 * w, 11 * w), (18 * w, 15.25 * w),
                (19 * w, 11 * w), (21.25 * w, 10 * w), (19 * w, 9 * w)), star)
    dr.polygon((
        (18 * w, 5.5 * w), (17.25 * w, 9.25 * w), (15.5 * w, 10 * w), (17.25 * w, 10.75 * w), (18 * w, 14.5 * w),
        (18.75 * w, 10.75 * w), (20.5 * w, 10 * w), (18.75 * w, 9.25 * w)), border)
    im.save('folio.png')


params = {'bookmark': '#d35b9e', 'spiral': '#885830', 'star': '#eded5d'}
folio(20, **params)
