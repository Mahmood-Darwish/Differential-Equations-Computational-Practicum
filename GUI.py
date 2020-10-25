from tkinter import *
from matplotlib import pyplot
import Solver

def draw_all_graphs():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x.get())
        y0 = float(box_y.get())
        X = float(box_end.get())
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
        X = 7
    if numberofsteps > 1000000 or numberofsteps < 10:
        numberofsteps = 10
    if X <= x0:
        X = x0 + 7
    res = Solver.EulerMethod(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Euler")
    res = Solver.ImprovedEulerMethod(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Improv. Euler")
    res = Solver.RungeKuttaMethod(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Runge-Kutta")
    res = Solver.solve(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Exact")
    pyplot.legend()
    pyplot.show()


def draw_all_error_graphs():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x.get())
        y0 = float(box_y.get())
        X = float(box_end.get())
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
        X = 7
    if numberofsteps > 1000000 or numberofsteps < 10:
        numberofsteps = 10
    if X <= x0:
        X = x0 + 7
    res = Solver.EulerMethod_error(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Euler")
    res = Solver.ImprovedEulerMethod_error(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Improv. Euler")
    res = Solver.RungeKuttaMethod_error(x0, y0, numberofsteps, X)
    pyplot.plot(res[0], res[1], label="Runge-Kutta")
    pyplot.legend()
    pyplot.show()

root = Tk()
root.title("Equation Solver")

root.minsize(400, 400)
root.maxsize(400, 400)

label_title = Label(root, text="f(x, y) = sec(x) - y tg(x)")
label_title.place(x=200, y=10, anchor="center")

box_steps = Entry(root)
box_steps.place(x=100, y=20)
box_steps.insert(END, '10')

label_steps = Label(root, text="number of steps:")
label_steps.place(x=5, y=20)

box_x = Entry(root)
box_x.place(x=100, y=40)
box_x.insert(END, '0')

label_x = Label(root, text="x0:")
label_x.place(x=5, y=40)

box_y = Entry(root)
box_y.place(x=100, y=60)
box_y.insert(END, '1')

label_y = Label(root, text="y0:")
label_y.place(x=5, y=60)

box_end = Entry(root)
box_end.place(x=100, y=80)
box_end.insert(END, '7')

label_end = Label(root, text="X:")
label_end.place(x=5, y=80)

draw_all_button = Button(root, text="draw all graphs", command=lambda: draw_all_graphs())
draw_all_button.place(anchor="center", x=200, y=200)

draw_all_error_button = Button(root, text="draw all error graphs", command=lambda: draw_all_error_graphs())
draw_all_error_button.place(anchor="center", x=200, y=225)

root.mainloop()
