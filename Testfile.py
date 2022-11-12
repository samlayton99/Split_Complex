from cmath import sqrt
import numpy as np
import math
import SplitComplexClass as scc
import matplotlib.pyplot as plt
from scipy.stats import shapiro

def generatenormalvar(mean, standarddeviation, refinement = 1000):
    """Generate a normal variable."""
    sum = 0
    for i in range(refinement):
        j = scc.split(0,1)
        sum = sum + j.rcollapse()
    real = (standarddeviation * float(sum) / sqrt(refinement)) + mean
    X = scc.split(real,0)
    return X.real

def createhistogram(mean, standarddeviation, refinement, count, bins, title = "Histogram", xlabel = "X", ylabel = "Frequency"):
    """Create a histogram."""
    X = np.zeros(count)
    for i in range(count):
        X[i] = generatenormalvar(mean, standarddeviation, refinement).real
    Y = np.zeros(count)
    #make a for loop that fills array Y with a random normal variable with mean and standard deviation
    for i in range(count):
        Y[i] = np.random.normal(mean, standarddeviation)
    plt.subplot(1,2,1)
    plt.hist(X, bins)
    plt.title("Split Complex Histogram")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.subplot(1,2,2)
    plt.hist(Y, bins)
    plt.title("Normal Variable Histogram")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()
    plt.show()
    return shapiro(X)

def test_normality():
    """Test the normality of the split complex normal variable."""
    print("Wait a second...")
    count = 1000
    X = np.zeros(count)
    for i in range(count):
        X[i] = generatenormalvar(0, 1, 10000).real

    print(shapiro(X))


def tester(a,b):
    """Test the add function."""
    for i in range(a,b):
        print(i)
        for j in range(a,b):
            print(j)
            for k in range(a,b):
                for l in range(a,b):
                    a1 = i
                    a2 = j
                    b1 = k
                    b2 = l
                    assert scc.split(a1,b1) + scc.split(a2,b2) == scc.split(a1+a2,b1+b2)


def transformation(split):
    """Transform a split complex variable."""
    return split * split


def plot_transformation(w,h,n, iter = 1, diamond = False):
    """Plot the transformation of a split complex variable."""
    X = np.linspace(-w/2,w/2,n)
    Y = np.linspace(-h/2,h/2,n)
    if diamond == True:
        X = np.linspace(-1,1,n)
        np.append(X, 0)
        w = 2
        h = 2



    for i in X:
        if diamond:
            if i == 0:
                sign = 0
            else:
                sign = abs(i) / i
            if sign < 0:
                topy = i + 1
                bottomy = -i - 1
                Y = np.array([topy, bottomy])
            elif sign == 0:
                Y = np.array([1,0,-1])
            else:
                topy = -i + 1
                bottomy = i - 1
                Y = np.array([topy, bottomy])

        for j in Y:
            input = scc.split(i,j)
            reallist = [input.real]
            imaglist = [input.imag]
            plt.plot(input.real, input.imag, 'ro')
            for k in range(iter):
                if k != 0:
                    plt.plot(input.real, input.imag, 'yo')
                input = transformation(input)
                reallist.append(input.real)
                imaglist.append(input.imag)
            
            plt.plot(reallist, imaglist)
            
            plt.plot(input.real, input.imag, 'bo')
    print(reallist, imaglist)
    plt.plot([0,0],[-h,h], 'k')
    plt.plot([-w,w],[0,0], 'k')
    plt.axis('equal')
    plt.tight_layout()
    plt.xlim(-w/2,w/2)
    plt.ylim(-h/2,h/2)
    plt.show()

plot_transformation(6,6,20,4, True)
Y = np.linspace(-3,3,10)

