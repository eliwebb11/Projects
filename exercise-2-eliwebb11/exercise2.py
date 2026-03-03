# %%
import numpy as np
import decimal


# %% [markdown]
# # CS 3513 Exercise 2   
# Spring 2025
#
# **Due 2/14/2025**.  Last day to submit with late penalty is 02/28/2025.
#
# See exercise2.pdf for additional informatoin beyond the comments in the code.
#
# Each question should be answered in the corresponding function.  Add your code to each function
# to evaluate your answers.
#
#

# %%
def Question1():
    print("Question 1")
    # inner function use for the question. 
    def foo(a,b,valueType=float) :
        term1 = valueType(333.75) * (b**6)  
        term2 = (a**2)  
        term3 =  11*(a**2) * (b**2) - (b**6) -121*(b**4) -2 
        term4 = valueType(5.5) * (b**8) 
        term5 = a/(2*b)
        return term1 + term2*term3 + term4 + term5 

    # values a and b for evaluation.  Provided as integers   
    a = 77617
    b = 33096

    # Evaluate the function foo(a,b) with a=77617 and b=33096 
    # using python's standard float type and python's decimal 
    # package with different values of decimal precision 
    # starting with precisions of 5, 10, and 20.  Print out 
    # the returned function value for each evaluation.   Continue 
    # increasing precision until you thikk the value is correct.  
    # Then decrease the precision to find the smallest decimal 
    # precision that is correct to the first 16 decimal digits.  
    # Print out that precision value at the end of Question1.  
    # To give you a starting point, decimal precission 5 is implemented 
    # below 

    D = decimal.Decimal  # short alias for the longer class name

    # first print foo(a,b) for float
    print("   float result is ",foo(a,b,float))
    # then decimal precision of 5
    decimal.getcontext().prec = 5 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 5, result is ",result)
    # repeat for decimal precision of 10
    decimal.getcontext().prec = 10 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 10, result is ",result)
    # repeat for decimal precision of 20
    decimal.getcontext().prec = 20 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 20, result is ",result)
    # repeat larger precisions until you think the value is correct
    decimal.getcontext().prec = 30 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 30, result is ",result)
    decimal.getcontext().prec = 40 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 40, result is ",result)
    decimal.getcontext().prec = 50 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 50, result is ",result)
    decimal.getcontext().prec = 60 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 60, result is ",result)
    # reduce precision to find smallest precision that is mostly corrrect (at least first 16 digits).
    decimal.getcontext().prec = 36 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 36, result is ",result)
    decimal.getcontext().prec = 37 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 37, result is ",result)
    decimal.getcontext().prec = 38 
    result = foo(D(a),D(b),D)
    print("   Using Decimal precision of 38, result is ",result)
    # print out the precision value you have found (replace ???).
    print("   Need at least ", "37", " decimal digits of precision to evaluate foo(a,b)")


# %%
def Question2():
    print("Question 2")
    # imports needed for Question 2
    from math import tanh
    from math import cosh
    # inner functions, only needed in Question 2
    def bar(x,c):
       return tanh(c*x)

    def d_bar(x,c):
       "first derivative of bar(x,c) with respect to x" 
       return c/pow(cosh(c*x),2)

    print("   Table notes :")
    print("      delta    : means absolute difference between bar(x,c) and bar(x+dx,c).")
    print("      ratio    : means delta/dx.")
    print("      devir    : means first derivative of bar(x,c) with respect to x.")
    print("      est diff : means the absolute difference between delta and the error estimate from ")
    print("                 first derivative times dx rule of thumb." )
    print()

    # add loop over x values of 1e-2, 1e-8, and 1e-16 
    for x in [1e-2, 1e-8, 1e-16]:
    #   add loop over values 1e6 and 1e12
        for loop_value in [1e6, 1e12]:
            dx = x/ loop_value
                 
    # before loop over c values, print out the headers
            print("   x={:5.2e}, dx={:5.2e}".format(x,dx))
            print("     {:^10s}   {:^8s} {:^13s};{:^10s};{:^10s};{:^10s}:{:^10s}".format("c","bar(x,c)","bar(x+dx,c)","delta","ratio","devir", "est diff" ))
    # add loop over c values of 1e1, 1e2, and 1e4.
            for c in [1e1, 1e2, 1e4]:
    #      replace with calculations and indent appropriately   
                a = bar(x, c)  # replace with call to bar
                b = bar(x + dx, c) # replace with call to bar using offset dx
                delta = abs(b - a)  # replace with absolute difference of a and b 
                ratio = delta/dx   # replace with delta divided by dx
                deriv = d_bar(x, c)  # replace with call to d_bar
                estdiff = abs(delta - abs(deriv * dx)) # replace with the absolute difference between delta and the absolute value of the derivative times dx
                print("      {:3.1e} =>  {:5.2e}   {:5.2e}   ; {:5.2e} ; {:5.2e} ; {:5.2e} : {:5.2e}".format(c,a,b,delta,ratio, deriv, estdiff ))

 

# %% [markdown]
# Question 3 will use the following two equations for calculating the x-intercept from a pair of points.
#
# \begin{align*}
# x &= \frac{x_1 y_0 - x_0 y_1 }{y_0-y_1}\\
# x &= x_0 - \frac{(x_1 - x_0) y_0}{y_1-y_0}
# \end{align*}
#
# The first equation should be implemented in inner function methodA.  The second in methodB.  You may wish to view exercise2.pdf to 
# see the equations if editing the py file or if the markdown equations are not rendered well in your browser.

   # %%
   # implement the two approaches to calculating the x-intercept 
def Question3():
    print("Question 3")

    def methodA(x0,y0,x1,y1):
        return ((x1 * y0) - (x0 * y1)) / (y0 - y1)

    def methodB(x0,y0,x1,y1):
        return x0 - (((x1 - x0) * y0) / (y1 - y0))

    D = decimal.Decimal  # short alias for the longer class name
    decimal.getcontext().prec = 3 
    # set x0, y0 from point (1.02, 3.32) as Decimal objects
    x0 = D('1.02')
    y0 = D('3.32')
    # set x1, y1 from point (1.31, 4.31) as Decimal objects
    x1 = D('1.31')
    y1 = D('4.31')
    # evaluate both methods; store and print the results
    a = methodA(x0,y0,x1,y1)
    b = methodB(x0,y0,x1,y1)
    print("   methodA's x-intercept is ",a)
    print("   methodB's x-intercept is ",b)
    # reset decimal prec
    decimal.getcontext().prec = 16

    # evaluate both methods and store the results
    precise_a = methodA(x0,y0,x1,y1)
    precise_b = methodB(x0,y0,x1,y1)
    # calculate the absolute and relative error of each method's initial calculation
    abs_a = abs(a - precise_a)
    rel_a = abs_a / abs(precise_a)
    abs_b = abs(b - precise_b)
    rel_b = abs_b / abs(precise_b)
    # replace ??? with calculated values
    print("   methodA's absolute error is ",abs_a, " and relative error is ",rel_a)
    print("   methodB's absolute error is ",abs_b, " and relative error is ",rel_b)

    # add a statement stating which formula is better and why you think that is.
    print("""   
   Multiline statement of discussion here.
   The formula that is better in my opinion is the formula from Method B. 
   I belive that Method B is better then method A because method B provides a closer and more precise answer then method A does. 
   Method A has more variablity, particularly when certain values are close to eachother causing potential lose of precision and rounding errors.
""")


# %%
if __name__ == "__main__":
    print("CS 3513, Spring 2025")
    print("Exercise 2")
    print("StudentName = ", "Eli Webb")  # replace ??? with your name
    print("GitHub Username = ", "eliwebb11")  # replace ??? with your GitHub username

    print()
    Question1()
    print()
    Question2()
    print()
    Question3()