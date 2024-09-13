def darkness(*args, **kwargs):
    



data = [('sculpture', 6), ('Siramalac', 11), ('HsiteF', 10), ('DiuqS', 9), ('hpargonorhc', 23)]
params = {'choice': 'cthulhu', 'transform': lambda x: f'{x[0][::-1]}-{x[1]}', 'to_sort': True}
print(darkness(*data, **params))