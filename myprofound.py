import tkinter
import random


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(obj)[0] <= 0:
        canvas.move(obj, step * N_X, 0)
    if canvas.coords(obj)[0] >= step * N_X:
        canvas.move(obj, -step * N_X, 0)
    if canvas.coords(obj)[1] <= 0:
        canvas.move(obj, 0, step * N_Y)
    if canvas.coords(obj)[1] >= step * N_Y:
        canvas.move(obj, 0, -step * N_Y)
    # Այստեղ անհրաժեշտ է անել այնպես, որ էկրանից հեռացած խաղացողը
    # դուրս գա հակառակ կողմից


def do_nothing(x):
    return


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Հաղթանակ")
        master.bind("<KeyPress>", do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(canvas, player, (0, -step))
        # Այստեղ պետք է լրացնել այն, ինչ անհրաժեշտ է, որպեսզի բոլոր այլ
    # ստեղներն աշխատեն
    if event.keysym == 'Down':
        move_wrap(canvas, player, (0, step))
    if event.keysym == 'Right':
        move_wrap(canvas, player, (step, 0))
    if event.keysym == 'Left':
        move_wrap(canvas, player, (-step, 0))
    check_move()


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
canvas = tkinter.Canvas(
    master, bg='blue', height=step * N_X, width=step * N_Y)

player_pos = (random.randint(1, N_X - 1) * step,
              random.randint(1, N_Y - 1) * step)
exit_pos = (random.randint(1, N_X - 1) * step,
            random.randint(1, N_Y - 1) * step)

player = canvas.create_oval(
    (player_pos[0], player_pos[1]),
    (player_pos[0] + step, player_pos[1] + step),
    fill='green'
)
exit = canvas.create_oval(
    (exit_pos[0], exit_pos[1]),
    (exit_pos[0] + step, exit_pos[1] + step),
    fill='yellow'
)

label = tkinter.Label(master, text="Գտիր ելքը")
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
