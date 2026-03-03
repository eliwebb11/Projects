import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize

def Question1():
    print("Question 1)")

    def f(p):
        integral, _ = integrate.quad(lambda x: np.sin(x) * np.cos(p * x), 0, np.pi)
        return integral

    ps = np.linspace(-10, 10, 400)
    fps = np.array([f(p) for p in ps])

    plt.figure()
    plt.plot(ps, fps, '-')
    plt.xlabel('p')
    plt.ylabel('f(p)')
    plt.title('Q1: f(p) vs p')
    plt.grid(True)
    plt.savefig('ex8q1plot.pdf')
    plt.close()

    res = optimize.minimize_scalar(f, bounds=(0, 10), method='bounded')
    print(f"    p = {res.x:.6f}")
    print(f"    f(p) = {res.fun:.6e}")
    print(f"    Number of function evaluates = {res.nfev}")
    print()

def Question2():
    print("Question 2)")

    plt.rcdefaults()
    plt.rcParams['figure.figsize'] = [4, 8]

    target = np.array([1.0, 2.0])
    def dist(x):
        y = x**2
        return np.hypot(x - target[0], y - target[1])

    xs = np.linspace(0, 2, 400)
    ds = dist(xs)

    plt.figure()
    plt.plot(xs, xs**2, 'r-', label='y=x²')
    plt.plot(xs, ds, 'b-', label='distance')
    plt.plot([1], [2], 'mo', label='(1,2)')
    plt.gca().set_aspect('equal')
    plt.xlabel('x')
    plt.ylabel('y or distance')
    plt.title('Q2: Parabola & Distance')
    plt.legend()
    plt.savefig(r'c:\Users\eliwe\OneDrive\Documents\GitHub\extra-credit-exercise-8-eliwebb11\ex8q2plot.pdf')
    plt.close()

    res = optimize.minimize_scalar(dist, method='brent')
    x_star = res.x
    y_star = x_star**2
    d_star = dist(x_star)

    print(f"    Solution point = ({x_star:.6f}, {y_star:.6f})")
    print(f"    Distance = {d_star:.6e}")
    print()

def Question3():
    print("Question 3)")
    def geometric_median(points, label):
        def f(x):
            return np.sum(np.linalg.norm(points - x, axis=1))

        x0 = points[0]

        res = optimize.minimize(f, x0, method='Nelder-Mead')
        x_med = res.x

        xmin, xmax = points[:,0].min(), points[:,0].max()
        ymin, ymax = points[:,1].min(), points[:,1].max()
        X, Y = np.meshgrid(np.linspace(xmin, xmax, 200),
                           np.linspace(ymin, ymax, 200))
        Z = np.zeros_like(X)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Z[i,j] = np.sum(np.hypot(points[:,0]-X[i,j], points[:,1]-Y[i,j]))

        plt.figure()
        cp = plt.contour(X, Y, Z, levels=30)
        plt.clabel(cp, inline=True, fontsize=8)
        plt.scatter(points[:,0], points[:,1], s=1.0, c='r', label='data')
        plt.plot(x_med[0], x_med[1], 'g*', markersize=12, label='median')
        plt.gca().set_aspect('equal')
        plt.title(f'Q3: Geometric Median ({label})')
        plt.legend()
        plt.savefig(rf'c:\Users\eliwe\OneDrive\Documents\GitHub\extra-credit-exercise-8-eliwebb11\ex8q3plot{label}.pdf')
        plt.close()
        print(f'ex8q3plot{label} created')

    for fname, label in [(r'c:\Users\eliwe\OneDrive\Documents\GitHub\extra-credit-exercise-8-eliwebb11\ex8pointsA.txt', 'A'),
                     (r'c:\Users\eliwe\OneDrive\Documents\GitHub\extra-credit-exercise-8-eliwebb11\ex8pointsB.txt', 'B')]:
        pts = np.loadtxt(fname)
        geometric_median(pts, label)

Question1()
Question2()
Question3()