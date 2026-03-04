import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import math

def Question1():
    print()
    print("Question 1:")
    def f(x):
        return np.exp(-x**2)

    # part a
    expected_value = math.erf(1) * math.sqrt(math.pi) / 2
    print()
    print("Part (a) integral is expected to be {:16.14f}".format(expected_value))

    # part b
    x = np.linspace(0, 1, 100)
    plt.plot(x, f(x))
    plt.title("f(x) = e^(-x^2)")
    plt.savefig("ex7q1plot.pdf")
    plt.close()

    # part c
    print()
    print("Part (c)")
    T = []
    for k in range(8):
        n = 2**k
        h = 1.0 / n
        x_vals = np.linspace(0, 1, n+1)
        y_vals = f(x_vals)
        T_k = h * (0.5 * y_vals[0] + np.sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
        T.append(T_k)
        print("   T({}) = {:16.14f} with error {:8.3e}".format(k, T_k, abs(T_k - expected_value)))

    # part d
    print()
    print("Part (d)")
    R = [[0]*8 for _ in range(8)]
    for i in range(8):
        R[i][0] = T[i]
    for j in range(1, 8):
        for i in range(j, 8):
            R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
    for i in range(8):
        print("   R[{}][{}] = {:16.14f} with error {:8.3e}".format(i, i, R[i][i], abs(R[i][i] - expected_value)))

    # part e
    quad_val, quad_err = integrate.quad(f, 0, 1)
    print()
    print("Part (e): quad estimate = {:16.14f} with error {:8.3e}".format(quad_val, abs(quad_val - expected_value)))

    # part f
    print()
    print("Part (f)")
    print("   Number of function evaluations for scipy quad: )".format(quad_err))
    print("   Number of function evaluations for romberg integration: {}".format(sum(2**i for i in range(8))))


def Question2():
    print()
    print("Question 2:")
    def f(x):
        return (200 / (2*x**3 - x**2)) * (5 * np.sin(20/x))**2

    # part a
    x = np.linspace(1.5, 4, 1000)
    plt.plot(x, f(x))
    plt.title("f(x) for Question 2")
    plt.savefig("ex7q2plot.pdf")
    plt.close()

    # part b
    quad_val, quad_err = integrate.quad(f, 1.5, 4)
    print()
    print("Part (b)")
    print("   quad estimate = {:16.14f}".format(quad_val))
    print("   quad absolute error = {:8.3e}".format(quad_err))

    # part c
    print()
    print("Part (c)")
    T = []
    for k in range(8):
        n = 2**k
        x_vals = np.linspace(1.5, 4, n+1)
        y_vals = f(x_vals)
        h = (4 - 1.5) / n
        T_k = h * (0.5 * y_vals[0] + np.sum(y_vals[1:-1]) + 0.5 * y_vals[-1])
        T.append(T_k)
        print("   T({}) = {:16.14f} with error {:8.3e}".format(k, T_k, abs(T_k - quad_val)))

    # part d
    print()
    print("Part (d)")
    R = [[0]*8 for _ in range(8)]
    for i in range(8):
        R[i][0] = T[i]
    for j in range(1, 8):
        for i in range(j, 8):
            R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
    for i in range(8):
        print("   R[{}][{}] = {:16.14f} with error {:8.3e}".format(i, i, R[i][i], abs(R[i][i] - quad_val)))

def Question3():
    print()
    print("Question 3:")

    v = np.array([0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75])
    p = np.array([89.8, 68.7, 55.0, 45.8, 39.3, 34.4, 30.5, 27.5, 26.0])
    
    # part a
    plt.figure()
    plt.plot(v, p, 
             linestyle='--', 
             marker='o', 
             markersize=12, 
             markerfacecolor='red', 
             markeredgecolor='black', 
             linewidth=2, 
             color='blue')
    plt.title("Pressure vs Volume")
    plt.xlabel("Volume (cubic inches)")
    plt.ylabel("Pressure (pounds per square inch)")
    plt.savefig("ex7q3plot.pdf")
    plt.close()
    
    # part b
    trapz_result = integrate.trapezoid(p, v)
    print()
    print("Part (b) Trapezoid integration result = {:16.14f} inch-pounds".format(trapz_result))
    
    # part c
    simpson_result = integrate.simpson(p, v)
    print()
    print("Part (c) Simpson integration result = {:16.14f} inch-pounds".format(simpson_result))
    
    # part d
    print()
    print("Part (d)")
    romb_result = integrate.romb(p, dx=v[1]-v[0], show=True)
    
    # part e
    print()
    print("Part (e): Between Romberg and Simpson I believe that Simpson provides a better method that gives a better estimate for this dataset. I believe this because it uses quadratic approximations which better shows the curvature seen in the pressure volume relationship. It also is better suited for a smaller data set.")

Question1()
Question2()
Question3()