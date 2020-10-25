import math


def F(x, C):
    return math.sin(x) + (C*math.cos(x))


def f(x, y):
    return (1 / math.cos(x)) - (y * math.tan(x))


def solve(x0, y0, numofsteps, X):
    C = (y0/math.cos(x0)) - math.tan(x0)
    res = [[], []]
    x = x0
    h = (X - x0) / numofsteps
    for i in range(numofsteps + 1):
        res[0].append(x)
        res[1].append(F(x, C))
        x += h
    return res


def EulerMethod(x0, y0, numofsteps, X):
    res = [[], []]
    y = y0
    x = x0
    h = (X - x0) / numofsteps
    for i in range(numofsteps + 1):
        res[0].append(x)
        res[1].append(y)
        y += f(x, y) * h
        x += h
    return res


def ImprovedEulerMethod(x0, y0, numofsteps, X):
    res = [[], []]
    y = y0
    x = x0
    h = (X - x0) / numofsteps
    for i in range(numofsteps + 1):
        res[0].append(x)
        res[1].append(y)
        y += (f(x, y) + f(x + h, y + (h * f(x, y)))) * (h / 2)
        x += h
    return res


def RungeKuttaMethod(x0, y0, numofsteps, X):
    def T(x, y, h):
        k1 = f(x, y)
        k2 = f(x + (h / 2), y + (0.5 * h * k1))
        k3 = f(x + (h / 2), y + (0.5 * h * k2))
        k4 = f(x + h, y + (h * k3))
        return (k1 + (2 * k2) + (2 * k3) + k4) / 6

    res = [[], []]
    y = y0
    x = x0
    h = (X - x0) / numofsteps
    for i in range(numofsteps + 1):
        res[0].append(x)
        res[1].append(y)
        y += T(x, y, h) * h
        x += h
    return res


def EulerMethod_error(x0, y0, numberofsteps, N):
    res1 = EulerMethod(x0, y0, numberofsteps, N)
    res2 = solve(x0, y0, numberofsteps, N)
    res = [[], []]
    for i in range(len(res1[0])):
        res[0].append(res1[0][i])
        res[1].append(abs(res1[1][i] - res2[1][i]))
    return res



def ImprovedEulerMethod_error(x0, y0, numberofsteps, N):
    res1 = ImprovedEulerMethod(x0, y0, numberofsteps, N)
    res2 = solve(x0, y0, numberofsteps, N)
    res = [[], []]
    for i in range(len(res1[0])):
        res[0].append(res1[0][i])
        res[1].append(abs(res1[1][i] - res2[1][i]))
    return res



def RungeKuttaMethod_error(x0, y0, numberofsteps, N):
    res1 = RungeKuttaMethod(x0, y0, numberofsteps, N)
    res2 = solve(x0, y0, numberofsteps, N)
    res = [[], []]
    for i in range(len(res1[0])):
        res[0].append(res1[0][i])
        res[1].append(abs(res1[1][i] - res2[1][i]))
    return res