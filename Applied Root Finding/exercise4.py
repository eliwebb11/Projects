import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import fsolve
from scipy.optimize import newton

# Question 1
def Question1():
    print("Question 1")
    Q = 1.2 # m^3/s = water volume rate of flow
    g = 9.81 # m^3/s = ravitational acceleration
    b = 1.8 # m = width of channel
    h0 = 0.6 # m = upstream water level
    H = 0.075 # m = height of bump
    # find h =? m = water level at bump

    def f(h):
        return ((Q**2 / (2 * g * b**2 * h0**2) + h0) - (Q**2 / (2 * g * b**2 * h**2) + h + H))
    
    h_vals = np.linspace(0.3, 0.6, 100)
    f_vals = [f(h) for h in h_vals]

    # Plot
    plt.plot(h_vals, f_vals)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('h (m)')
    plt.ylabel('Equation value')
    plt.grid(True)
    plt.savefig('ex4q1plot.pdf')
    plt.close()

    # Brents Method
    h_root = brentq(f, 0.4, 0.6)
    print(f"Solution: h = {h_root:.4f} m")
    print("Method: Brent's method")

# Question 2
def Question2():
    print("Question 2")
    def pipe_equation(alpha, w0=10, w1=8, theta=np.pi/2):
        phi = np.pi - alpha - theta
        return (w0 * np.cos(alpha) / np.sin(alpha)**2) - (w1 * np.cos(phi) / np.sin(phi)**2)

    angles = [np.pi/2, 3*np.pi/5, 2*np.pi/3]
    labels = ['a', 'b', 'c']
    for i, theta in enumerate(angles):
        alpha_vals = np.linspace(0.1, np.pi/2, 100)
        f_vals = [pipe_equation(alpha, theta=theta) for alpha in alpha_vals]
        
        # Plot
        plt.plot(alpha_vals, f_vals)
        plt.axhline(0, color='red', linestyle='--')
        plt.xlabel('Alpha')
        plt.ylabel('Equation Value')
        plt.grid(True)
        plt.savefig(f'ex4q2{labels[i]}plot.pdf')
        plt.close()
        
        # fsolve
        alpha_solution = fsolve(pipe_equation, 0.5, args=(10, 8, theta))[0]
        L = 10 / np.sin(alpha_solution) + 8 / np.sin(np.pi - alpha_solution - theta)
        print(f'{chr(97+i)}: Alpha = {alpha_solution:.4f} L = {L:.4f}')

    print("Method: fsolve")

# Question 3
def Question3():
    P = 2.0  # atm = pressure in atmospheres
    T = 313  # K =  temperature in degrees Kelvin
    n = 1.0  # mol = amount of gas in moles
    R = 0.082057366  # L · atm/(K · mol) = universal gas constant
    a = 6.254198  # atm · L^2 / mol^2 = correction for intermolecular attractive force
    b = 0.05422  # L/mol = correction incompressible intrinsic volume

    def f(V):
        return (P + a * n**2 / V**2) * (V - n * b) - n * R * T

    V_vals = np.linspace(10, 20, 100)
    f_vals = [f(V) for V in V_vals]

    # Plot
    plt.plot(V_vals, f_vals)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('V (L)')
    plt.ylabel('Equation value')
    plt.grid(True)
    plt.savefig('ex4q3plot.pdf')
    plt.close()

    # Newton Raphson
    V_root = newton(f, 12)
    print(f"Solution: V = {V_root:.2f} L")
    print("Method: Newton Raphson")
    print("Initial Value: 12")
    
if __name__ == "__main__" :
    print("CS 3513, Spring 2025")
    print("Exercise 4")
    print("StudentName = ", "Eli Webb")
    print("GitHub Username = ", "eliwebb11")
    print()
    Question1()
    print()
    Question2()
    print()
    Question3()