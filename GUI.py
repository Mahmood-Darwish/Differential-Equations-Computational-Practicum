from tkinter import *
from tkinter import ttk
from matplotlib import pyplot
from Solver import solver

class GUI:
    def draw_all_graphs(self):
        try:
            numberofsteps = int(self.box_steps.get())
            x0 = float(self.box_x.get())
            y0 = float(self.box_y.get())
            X = float(self.box_end.get())
        except:
            numberofsteps = 10
            x0 = 0
            y0 = 1
            X = 7
        if numberofsteps > 1000000 or numberofsteps < 10:
            numberofsteps = 10
        if X <= x0:
            X = x0 + 7
        res = solver.EulerMethod(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Euler")
        res = solver.ImprovedEulerMethod(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Improv. Euler")
        res = solver.RungeKuttaMethod(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Runge-Kutta")
        res = solver.solve(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Exact")
        pyplot.legend()
        pyplot.show()


    def draw_all_error_graphs(self):
        try:
            numberofsteps = int(self.box_steps.get())
            x0 = float(self.box_x.get())
            y0 = float(self.box_y.get())
            X = float(self.box_end.get())
        except:
            numberofsteps = 10
            x0 = 0
            y0 = 1
            X = 7
        if numberofsteps > 1000000 or numberofsteps < 10:
            numberofsteps = 10
        if X <= x0:
            X = x0 + 7
        res = solver.EulerMethod_error(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Euler")
        res = solver.ImprovedEulerMethod_error(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Improv. Euler")
        res = solver.RungeKuttaMethod_error(x0, y0, numberofsteps, X)
        pyplot.plot(res[0], res[1], label="Runge-Kutta")
        pyplot.legend()
        pyplot.show()


    def analyse(self):
        try:
            n0 = int(self.box_n0.get())
            n1 = int(self.box_n1.get())
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
            res_Euler[1].append(solver.EulerMethod_maxerror(i))
        res_ImprovedEuler = [[], []]
        for i in range(n0, n1 + 1):
            res_ImprovedEuler[0].append(i)
            res_ImprovedEuler[1].append(solver.ImprovedEulerMethod_maxerror(i))
        res_RungeKutta = [[], []]
        for i in range(n0, n1 + 1):
            res_RungeKutta[0].append(i)
            res_RungeKutta[1].append(solver.RungeKuttaMethod_maxerror(i))
        pyplot.plot(res_Euler[0], res_Euler[1], label="Euler")
        pyplot.plot(res_ImprovedEuler[0], res_ImprovedEuler[1], label="Improved Euler")
        pyplot.plot(res_RungeKutta[0], res_RungeKutta[1], label="Runge-Kutta")
        pyplot.legend()
        pyplot.show()

    def start(self):
        self.root = Tk()
        self.root.title("Equation Solver")

        self.root.minsize(400, 400)
        self.root.maxsize(400, 400)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()
        self.Frame1 = Frame(self.notebook, height=500, width=500)
        self.Frame2 = Frame(self.notebook, height=500, width=500)
        self.Frame1.pack()
        self.Frame2.pack()
        self.notebook.add(self.Frame1, text="Graphing")
        self.notebook.add(self.Frame2, text="Error Analysis")

        self.label_title = Label(self.Frame1, text="f(x, y) = sec(x) - y tg(x)")
        self.label_title.place(x=200, y=10, anchor="center")

        self.box_steps = Entry(self.Frame1)
        self.box_steps.place(x=100, y=20)
        self.box_steps.insert(END, '10')

        self.label_steps = Label(self.Frame1, text="number of steps:")
        self.label_steps.place(x=5, y=20)

        self.box_x = Entry(self.Frame1)
        self.box_x.place(x=100, y=40)
        self.box_x.insert(END, '0')

        self.label_x = Label(self.Frame1, text="x0:")
        self.label_x.place(x=5, y=40)

        self.box_y = Entry(self.Frame1)
        self.box_y.place(x=100, y=60)
        self.box_y.insert(END, '1')

        self.label_y = Label(self.Frame1, text="y0:")
        self.label_y.place(x=5, y=60)

        self.box_end = Entry(self.Frame1)
        self.box_end.place(x=100, y=80)
        self.box_end.insert(END, '7')

        self.label_end = Label(self.Frame1, text="X:")
        self.label_end.place(x=5, y=80)

        self.draw_all_button = Button(self.Frame1, text="draw all graphs", command=lambda: self.draw_all_graphs())
        self.draw_all_button.place(anchor="center", x=200, y=200)

        self.draw_all_error_button = Button(self.Frame1, text="draw all error graphs", command=lambda: self.draw_all_error_graphs())
        self.draw_all_error_button.place(anchor="center", x=200, y=225)

        self.box_n0 = Entry(self.Frame2)
        self.box_n0.place(x=50, y=20)
        self.box_n0.insert(END, '10')

        self.label_n0 = Label(self.Frame2, text="n_start:")
        self.label_n0.place(x=5, y=20)

        self.box_n1 = Entry(self.Frame2)
        self.box_n1.place(x=53, y=42)
        self.box_n1.insert(END, '100')

        self.label_n1 = Label(self.Frame2, text="n_finish:")
        self.label_n1.place(x=5, y=42)

        self.analyse_button = Button(self.Frame2, text="Analyse", command=lambda: self.analyse())
        self.analyse_button.place(anchor="center", x=200, y=200)


        self.root.mainloop()

a = GUI()
a.start()