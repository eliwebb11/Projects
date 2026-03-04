# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import math
import numpy as np

# %% [markdown]
# # CS 3513 Exercise 1   
# Spring 2025
#
# **Due 1/31/2025**.  Last day to submit with late penalty: 2/14/2025  
#


# %% [markdown]
# Each question should be answered in the corresponding function. 
# Add to each function code to evaluate your answer.

# %%
# Use the error progation estimation rule of thumbs to make the following
# estimates in function Question1.  Each is worth 2 points
def Question1():
    print("Question 1")
    # Let x = 75 +/ 0.5
    x = 75.0
    # (a) What is the absolute and the relative error of x?
    abs_err_x = 0.5 # replace with correct value or expression
    rel_err_x = 0.5 / 75.0 # replace with correct value or expression
    print("  (a) abs_err_x = {:9.8f},         rel_err_x = {:9.8f}".format(abs_err_x,rel_err_x))
    # (b) What is the absolute and the relative error of x+x ?
    abs_err_x_plus_x = 1.0 # replace with correct value or expression
    rel_err_x_plus_x = 1.0 / 150.0 # replace with correct value or expression
    print("  (b) abs_err_x_plus_x = {:9.8f},  rel_err_x_plus_x = {:9.8f}".format(abs_err_x_plus_x,rel_err_x_plus_x))
    # (c) What is the absolute and the relative error of x*x ?
    rel_err_x_times_x = (0.5 / 75.0) + (0.5 / 75.0) # replace with correct value or expression
    abs_err_x_times_x = 75 # replace with correct value or expression
    print("  (c) abs_err_x_times_x = {:9.8f}, rel_err_x_times_x = {:9.8f}".format(abs_err_x_times_x,rel_err_x_times_x))
    # (d) if y = f(x) = 4 x^3 -3 x^2 + 1, what is an approxiamtion of absolute and relative error of y=f(x)
    y = 4 * (x**3) - 3 * (x**2) + 1
    f_prime_at_x = 12 * (x**2) - 6 * x # f_prime_at_x = f'(75), the first derivate evaluate at x;  replace with correct value or expression
    abs_err_y = (12 * (x**2) - 6 * x) * 0.5 # replace with correct value or expression
    rel_err_y = abs_err_y / y # replace with correct expression
    print("  (d) f_prime_at_x = {:9.8f}".format(f_prime_at_x))
    print("      abs_err_y = {:9.8f},         rel_err_y = {:9.8f}".format(abs_err_y,rel_err_y))


# %%
def Question2():
    # worth 5 points 
    print("Question 2")
    x=1.0
    x_hex_string = x.hex()
    print("   Using x={}, with hexadecimal string {}".format(x,x_hex_string))
    gapX = np.spacing(x)
    print("      gap at x ={}".format(gapX))

    # complete the following expression, use variable name to determine expression
    x_plus_gapX = x + gapX # replace with correct value or expression
    x_plus_one_half_gapX = x + gapX/2 # replace with correct value or expression
    x_minus_one_half_gapX = x - gapX/2 # replace with correct value or expression
    x_minus_one_fourth_gapX = x - gapX/4 # replace with correct value or expression
    print("      x_plus_gapX={}, with hexadecimal string {}".format(x_plus_gapX,x_plus_gapX.hex()))
    print("      x_plus_one_half_gapX={}, with hexadecimal string {}".format(x_plus_one_half_gapX,x_plus_one_half_gapX.hex()))
    print("      x_minus_one_half_gapX={}, with hexadecimal string {}".format(x_minus_one_half_gapX,x_minus_one_half_gapX.hex()))
    print("      x_minus_one_fourth_gapX={}, with hexadecimal string {}".format(x_minus_one_fourth_gapX,x_minus_one_fourth_gapX.hex()))

    x_hex_string ='0x1.0000000000000p+300' # = 2^300
    x = float.fromhex(x_hex_string)
    print("   Using x={:18.16e}, with hexadecimal string {}".format(x,x_hex_string))
    gapX = np.spacing(x)
    print("      gap at x ={}".format(gapX))
    hex_string_x_next_value = "0x1.0000000000000p+301" # replace by copying and modifying x_hex_string to the next larger value
    print("      hex_string_x_next_value ={} with value {:18.16e}".format(hex_string_x_next_value, float.fromhex(hex_string_x_next_value)))
    hex_string_x_prev_value = "0x1.0000000000000p+299" # replace by copying and modifying x_hex_string to the closest smaller value
    print("      hex_string_x_prev_value ={} with value {:18.16e}".format(hex_string_x_prev_value, float.fromhex(hex_string_x_prev_value)))

# %%
    


# %% [markdown]
# Question 3
# The value of $1/e$ is given by the series
# $$  \frac{1}{e} = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!} = 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + - \cdots $$
#
# Use the above series estimate $1/e$ to within a specified tolerance.  
# Implement your series estimate in the EstimateEInverse function that follows.
# the function Question2 calls your implementation and print results

# %%
def EstimateEInverse(tolerance=1e-12,maxIterations=100):
    # initialize current estimate to first two terms in series: 1 - (1/1!) is zero
    curEst = 0.0
    n = 2 # first two terms of series is used to initial variables, next iteration is at n=2
    # add any other initialization that you may need here
    factoral = 1

    # implement your iteration to evaluate the rest of the series until the 
    # absolute value of next term of the series is less than tolerance. 
    # while n < maxIterations  and  your check for convergence within tolerance : 
    #     add code for while loop
    #     note: your should update the factorial incrementally with loop.  That
    #           is, 3! is the previous 2! times 3.
    while n < maxIterations:

        factoral *= n
        next_term = ((-1)**n) / factoral 

        if abs(next_term) < tolerance:
            break

        curEst += next_term
        n += 1

    return curEst;

# %%
def Question3():
    # worth 8 points 
    print("Question 3")
    library_inv_e = math.exp(-1)
    tol = 1e-7
    inv_e_estimate = EstimateEInverse(tolerance=tol)
    print("  Using tolerance {:4.2e}".format(tol))
    print("     Estimate 1/e = {:17.16f} with absolute error {:3.2e}".format(inv_e_estimate,abs(library_inv_e-inv_e_estimate)))
    tol = 1e-12
    inv_e_estimate = EstimateEInverse(tolerance=tol)
    print("  Using tolerance {:4.2e}".format(tol))
    print("     Estimate 1/e = {:17.16f} with absolute error {:3.2e}".format(inv_e_estimate,abs(library_inv_e-inv_e_estimate)))


# %%

# %%
# Using standard approach to execute code if running as a script
# instead of import as module. 
# Like the main method of Java
if __name__ == "__main__" :
    print("CS 3513, Spring 2025")
    print("Exercise 1")
    print("StudentName = ", "Eli Webb")  # replace ??? with your name
    print("GitHub Username = ", "eliwebb11")  # replace ??? with your GitHub username
    Question1()
    Question2()
    Question3()

