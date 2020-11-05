import matplotlib.pyplot as plt

def plot (xarr,yarr):
    plt.plot(xarr,yarr)
    plt.xlabel('n - array size')
    plt.ylabel('iterations - repeat counts')
    plt.title("Plot of size vs. Iterations")
    plt.show()