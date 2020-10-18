from tkinter import *
import matplotlib
import Solver


def draw_graph():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x)
        y0 = float(box_y)
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
    if numberofsteps > 10000 or numberofsteps < 1:
        numberofsteps = 10
    if x0 > 7:
        x0 = 0
    if method == "Euler’s method":
        matplotlib.pyplot.title("Euler's method")
        res = Solver.EulerMethod(x0, y0, numberofsteps)
    if method == "Improved Euler’s method":
        matplotlib.pyplot.title("Improved Euler's method")
        res = Solver.ImprovedEulerMethod(x0, y0, numberofsteps)
    if method == "Runge-Kutta method":
        matplotlib.pyplot.title("Runge-Kutta method")
        res = Solver.RungeKuttaMethod(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.solve(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    matplotlib.pyplot.legend("Approx", "Exact")
    matplotlib.pyplot.show()


def draw_error_graph():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x)
        y0 = float(box_y)
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
    if numberofsteps > 10000 or numberofsteps < 1:
        numberofsteps = 10
    if x0 > 7:
        x0 = 0
    if method == "Euler’s method":
        matplotlib.pyplot.title("Euler's method error")
        res = Solver.EulerMethod_error(x0, y0, numberofsteps)
    if method == "Improved Euler’s method":
        matplotlib.pyplot.title("Improved Euler's method error")
        res = Solver.ImprovedEulerMethod_error(x0, y0, numberofsteps)
    if method == "Runge-Kutta method":
        matplotlib.pyplot.title("Runge-Kutta method error")
        res = Solver.RungeKuttaMethod_error(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    matplotlib.pyplot.show()


def draw_all_graphs():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x)
        y0 = float(box_y)
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
    if numberofsteps > 10000 or numberofsteps < 1:
        numberofsteps = 10
    if x0 > 7:
        x0 = 0
    res = Solver.EulerMethod(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.ImprovedEulerMethod(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.RungeKuttaMethod(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.solve(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    matplotlib.pyplot.legend("Euler", "Improv. Euler", "R-K", "Exact")
    matplotlib.pyplot.show()


def draw_all_error_graphs():
    try:
        numberofsteps = int(box_steps.get())
        x0 = float(box_x)
        y0 = float(box_y)
    except:
        numberofsteps = 10
        x0 = 0
        y0 = 1
    if numberofsteps > 10000 or numberofsteps < 1:
        numberofsteps = 10
    if x0 > 7:
        x0 = 0
    matplotlib.pyplot.title("All errors")
    res = Solver.EulerMethod_error(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.ImprovedEulerMethod_error(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    res = Solver.RungeKuttaMethod_error(x0, y0, numberofsteps)
    matplotlib.pyplot.plot(res[0], res[1])
    matplotlib.pyplot.legend("Euler", "Improv. Euler", "R-K")
    matplotlib.pyplot.show()

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

method = StringVar(root)
choices = {"Improved Euler’s method", "Runge-Kutta method", "Euler’s method"}
method.set("Euler's method")
popupMenu = OptionMenu(root, method, *choices)
popupMenu.place(x=5, y=80)

draw_button = Button(root, text="draw graph", command=lambda: draw_graph())
draw_button.place(anchor="center", x=200, y=150)

draw_error_button = Button(root, text="draw error graph", command=lambda: draw_error_graph())
draw_error_button.place(anchor="center", x=200, y=175)

draw_all_button = Button(root, text="draw all graphs", command=lambda: draw_all_graphs())
draw_all_button.place(anchor="center", x=200, y=200)

draw_all_error_button = Button(root, text="draw all error graphs", command=lambda: draw_all_error_graphs())
draw_all_error_button.place(anchor="center", x=200, y=225)

root.mainloop()
