# from tkinter import *
# from tkinter.messagebox import *
#
# dic = {'Ալավերդյան': [3, 2, 1, {'Թովմասյան Սերգո': 10, 'Նազարյան Գագիկ': 10}, range(10, 13)],
#        'Մատինյան': [2, 2, 0, {'Խառատյան Նունե': -12, 'Կարապետյան Մանվել': -11}, range(7, 10)]
#        }
#
# print('Hello my friend!')
#
# name = input('what is your name?: ')
# surname = input('What is your surname?: ')
# clas = int(input('what is your class?: '))
# name_book = input('What book do you wanna take: ').lower()
#
# names = []
# s = []
# if not name_book in dic:
#     print("we don't have this book")
# else:
#     for i in dic[name_book]:
#         names.append(i)
#
#     if clas in names[4]:
#         if names[1] == names[0]:
#             for i, j in names[3].items():
#                 if abs(j) < 10:
#                     s.append(i)
#             if len(s) == 1:
#                 print(f'Դուք կարող եք վերցնել այս գիրքը {s} ից։')
#             elif len(s) == 0:
#                 print('Ազատ գրքեր չկան։')
#             else:
#                 print(f'Դուք կարող եք վերցնել այս գրքերը հետևյալ մարդկանցից՝ {s}։')
#
#         else:
#             print(f'{names[2]}: այսքան գիրք ազատ է, կարող եք վերցնել գրադարանից։')
#     else:
#         print("you can't take this book")
#
# main = Tk()
#
# main['bg'] = '#fafafa'
# main.title('Nobody')
# main.resizable(height=True, width=True)
# btn = Button()
# btn.place()
# main.mainloop()

from tkinter import *
from tkinter.messagebox import *


def btn_delete():
    name_book.delete(0, 'end')
    age_user.delete(0, 'end')


def btn_click():
    name = name_book.get()
    age = int(age_user.get())
    '''info_str = f'{str(name)}, {str(age)}'
    messagebox.showinfo(title = 'esiminch', message = info_str)'''

    dic = {'alaverdyan': [3, 2, 1, {'Tovmasyan Sergo': 10, 'Nazaryan Gagik': 10}, [10, 11, 12]],
           'matinyan': [2, 2, 0, {'Kharatyan Nune': 12, 'Karapetyan manvel': 11}, [7, 8, 9]]
           }

    names = []
    s = []
    if not name in dic:
        ka_chka.insert(0, 'we dont have this book')

    else:
        for i in dic[name]:
            names.append(i)
        if age in names[4]:
            if names[1] == names[0]:
                for i, j in names[3].items():
                    if j < 10:
                        s.append(i)
                if len(s) == 1:
                    mardik.insert(0, 'duq karoxeq vercnel ays girqy {s} ic')
                    ka_chka.insert(0, 'tvyal girqy arka e gradaranum')
                elif len(s) == 0:
                    ka_chka, insert(0, 'azat grqer chkan')
                else:
                    mardik.insert(0, f'duq karoxeq vercnelay grqery hetevyal mardkancic, {s}')
                    ka_chka.insert(0, 'tvyal girqy arka e gradaranum')

            else:
                qanak.insert(0, str({names[2]}))
                mardik.insert(0, 'aysqan girqy azat e, karox eq vercnel gradaranic')
                ka_chka.insert(0, 'ayd grqi voch bolor kopianern en zbaxvac')
        else:
            ka_chka.insert(0, 'duq cheq karox vercnel ays girqy')


GD = Tk()

GD['bg'] = '#fafafa'
GD.title('Gradaran')
GD.wm_attributes('-alpha', 0.8)
GD.geometry('600x450')

canvas = Canvas(GD, height=True, width=True)
canvas.pack()

frame = Frame(GD, bg='#fafafa')
frame.place(relwidth=1, relheight=1)

title1 = Label(frame, text='grqi anuny')
title1.place(relx=0.05, rely=0.05)
title2 = Label(frame, text='dzer dasarany')
title2.place(relx=0.05, rely=0.1)
title3 = Label(frame, text='exelutyun')
title3.place(relx=0.05, rely=0.15)
title4 = Label(frame, text='tvyal grqi qanaky')
title4.place(relx=0.05, rely=0.2)
title5 = Label(frame, text='ay mardik voroncic karox eq vercnel ays girqy')
title5.place(relx=0.05, rely=0.25)

btn1 = Button(frame, text='show', bg='red', command=btn_click)
btn1.place(relx=0.05, rely=0.85, relheight=0.05, relwidth=0.1)
btn2 = Button(frame, text='delete', bg='red', command=btn_delete)
btn2.place(rely=0.85, relx=0.85, relheight=0.05, relwidth=0.1)

name_book = Entry(frame, bg='white')
name_book.place(rely=0.05, relx=0.5, relwidth=0.45)
age_user = Entry(frame, bg='white')
age_user.place(relx=0.5, rely=0.1, relwidth=0.45)
ka_chka = Entry(frame, bg='white')
ka_chka.place(relx=0.5, rely=0.15, relwidth=0.45)
qanak = Entry(frame, bg='white')
qanak.place(relx=0.5, rely=0.2, relwidth=0.45)
mardik = Entry(frame, bg='white')
mardik.place(relx=0.5, rely=0.25, relwidth=0.45)
GD.mainloop()