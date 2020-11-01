from tkinter import *
from tkinter import ttk
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


def analyse():
    try:
        n0 = int(box_n0.get())
        n1 = int(box_n1.get())
    except:
        n0 = 10
        n1 = 100
    if n0 < 1:
        n0 = 10
    if n1 < n0:
        n1 = n0 + 100
    res_Euler = [[], []]
    for i in range(n0, n1 + 1):
        res_Euler[0].append(i)
        res_Euler[1].append(Solver.EulerMethod_maxerror(i))
    res_ImprovedEuler = [[], []]
    for i in range(n0, n1 + 1):
        res_ImprovedEuler[0].append(i)
        res_ImprovedEuler[1].append(Solver.ImprovedEulerMethod_maxerror(i))
    res_RungeKutta = [[], []]
    for i in range(n0, n1 + 1):
        res_RungeKutta[0].append(i)
        res_RungeKutta[1].append(Solver.RungeKuttaMethod_maxerror(i))
    pyplot.plot(res_Euler[0], res_Euler[1], label="Euler")
    pyplot.plot(res_ImprovedEuler[0], res_ImprovedEuler[1], label="Improved Euler")
    pyplot.plot(res_RungeKutta[0], res_RungeKutta[1], label="Runge-Kutta")
    pyplot.legend()
    pyplot.show()


root = Tk()
root.title("Equation Solver")

root.minsize(400, 400)
root.maxsize(400, 400)

notebook = ttk.Notebook(root)
notebook.pack()
Frame1 = Frame(notebook, height=500, width=500)
Frame2 = Frame(notebook, height=500, width=500)
Frame1.pack()
Frame2.pack()
notebook.add(Frame1, text="Graphing")
notebook.add(Frame2, text="Error Analysis")

label_title = Label(Frame1, text="f(x, y) = sec(x) - y tg(x)")
label_title.place(x=200, y=10, anchor="center")

box_steps = Entry(Frame1)
box_steps.place(x=100, y=20)
box_steps.insert(END, '10')

label_steps = Label(Frame1, text="number of steps:")
label_steps.place(x=5, y=20)

box_x = Entry(Frame1)
box_x.place(x=100, y=40)
box_x.insert(END, '0')

label_x = Label(Frame1, text="x0:")
label_x.place(x=5, y=40)

box_y = Entry(Frame1)
box_y.place(x=100, y=60)
box_y.insert(END, '1')

label_y = Label(Frame1, text="y0:")
label_y.place(x=5, y=60)

box_end = Entry(Frame1)
box_end.place(x=100, y=80)
box_end.insert(END, '7')

label_end = Label(Frame1, text="X:")
label_end.place(x=5, y=80)

draw_all_button = Button(Frame1, text="draw all graphs", command=lambda: draw_all_graphs())
draw_all_button.place(anchor="center", x=200, y=200)

draw_all_error_button = Button(Frame1, text="draw all error graphs", command=lambda: draw_all_error_graphs())
draw_all_error_button.place(anchor="center", x=200, y=225)

box_n0 = Entry(Frame2)
box_n0.place(x=50, y=20)
box_n0.insert(END, '10')

label_n0 = Label(Frame2, text="n_start:")
label_n0.place(x=5, y=20)

box_n1 = Entry(Frame2)
box_n1.place(x=53, y=42)
box_n1.insert(END, '100')

label_n1 = Label(Frame2, text="n_finish:")
label_n1.place(x=5, y=42)

analyse_button = Button(Frame2, text="Analyse", command=lambda: analyse())
analyse_button.place(anchor="center", x=200, y=200)


root.mainloop()
