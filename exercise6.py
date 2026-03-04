import math
import numpy as np
import jax.numpy as jnp
from jax import grad


def Question1():
    # part a
    t = math.pi / 5
    analytical = 1 / (math.cosh(t) ** 2)
    print("Part (a) is {:16.14f}".format(analytical))

    def f(x):
        return math.tanh(x)

    # part b
    step = math.pi / 10

    derivative_h1 = (f(t + step) - f(t - step)) / (2 * step)
    print("Part (b) estimate is {:16.14f}".format(derivative_h1))

    # part c
    step = math.pi / 20

    derivative_h2 = (f(t + step) - f(t - step)) / (2 * step)
    print("Part (c) estimate is {:16.14f}".format(derivative_h2))

    # part d
    derivative_richardson = (4 * derivative_h2 - derivative_h1) / 3
    print("Part (d) estimate is {:16.14f}".format(derivative_richardson))

    # part e
    def f_jax(x):
        return jnp.tanh(x)

    deriv_jax = grad(f_jax)
    derivative_auto = float(deriv_jax(t))
    print("Part (e) estimate is {:16.14f}".format(derivative_auto))

    # part f
    second_derivative_h2 = (f(t + step) - 2 * f(t) + f(t - step)) / (step ** 2)
    print("Part (f) estimate is {:16.14f}".format(second_derivative_h2))

    # part g
    deriv2_jax = grad(deriv_jax)
    second_derivative_auto = float(deriv2_jax(t))
    print("Part (g) estimate is {:16.14f}".format(second_derivative_auto))

def Question2():
    # Given data
    t = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16], dtype=float)
    x = np.array([0, 0.7, 1.8, 3.4, 5.1, 6.3, 7.3, 8.0, 8.4], dtype=float)

    # part a
    i = np.where(t == 10)[0][0]
    velocity = (x[i + 1] - x[i - 1]) / (t[i + 1] - t[i - 1])
    print("Part (a) estimate is {:.3f}".format(velocity))

    # part b
    acceleration = (x[i + 1] - 2 * x[i] + x[i - 1]) / ((t[i + 1] - t[i]) ** 2)
    print("Part (b) estimate is {:.3f}".format(acceleration))

    # part c
    velocity = np.gradient(x, t)
    print("Part (c) estimate is {:.3f}".format(velocity[i]))

print("Question 1)")
Question1()
print()
print("Question 2)")
Question2()