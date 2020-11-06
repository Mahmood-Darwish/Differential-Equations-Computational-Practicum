import math


def F(x, C):
    return math.sin(x) + (C*math.cos(x))


def f(x, y):
    return (1 / math.cos(x)) - (y * math.tan(x))

class solver():
    @staticmethod
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


    @staticmethod
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


    @staticmethod
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


    @staticmethod
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

    @staticmethod
    def EulerMethod_error(x0, y0, numberofsteps, N):
        res1 = solver.EulerMethod(x0, y0, numberofsteps, N)
        res2 = solver.solve(x0, y0, numberofsteps, N)
        res = [[], []]
        for i in range(len(res1[0])):
            res[0].append(res1[0][i])
            res[1].append(abs(res1[1][i] - res2[1][i]))
        return res

    @staticmethod
    def ImprovedEulerMethod_error(x0, y0, numberofsteps, N):
        res1 = solver.ImprovedEulerMethod(x0, y0, numberofsteps, N)
        res2 = solver.solve(x0, y0, numberofsteps, N)
        res = [[], []]
        for i in range(len(res1[0])):
            res[0].append(res1[0][i])
            res[1].append(abs(res1[1][i] - res2[1][i]))
        return res

    @staticmethod
    def RungeKuttaMethod_error(x0, y0, numberofsteps, N):
        res1 = solver.RungeKuttaMethod(x0, y0, numberofsteps, N)
        res2 = solver.solve(x0, y0, numberofsteps, N)
        res = [[], []]
        for i in range(len(res1[0])):
            res[0].append(res1[0][i])
            res[1].append(abs(res1[1][i] - res2[1][i]))
        return res


    @staticmethod
    def EulerMethod_maxerror(n):
        res1 = solver.solve(0, 1, n, 1.5)
        res2 = solver.EulerMethod(0, 1, n, 1.5)
        ans = -1
        for i in range(len(res1[0])):
            ans = max(ans, abs(res1[1][i] - res2[1][i]))
        return ans


    @staticmethod
    def ImprovedEulerMethod_maxerror(n):
        res1 = solver.solve(0, 1, n, 1.5)
        res2 = solver.ImprovedEulerMethod(0, 1, n, 1.5)
        ans = -1
        for i in range(len(res1[0])):
            ans = max(ans, abs(res1[1][i] - res2[1][i]))
        return ans

    @staticmethod
    def RungeKuttaMethod_maxerror(n):
        res1 = solver.solve(0, 1, n, 1.5)
        res2 = solver.RungeKuttaMethod(0, 1, n, 1.5)
        ans = -1
        for i in range(len(res1[0])):
            ans = max(ans, abs(res1[1][i] - res2[1][i]))
        return ans
