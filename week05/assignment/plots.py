'''
To import matplotlib: https://matplotlib.org/stable/users/installing/index.html
'''
import matplotlib.pyplot as plt

class Plots:
    """ Create plots for reports """
    def __init__(self, title=''):
        self._title = title

    def line(self, xdata, ydata,
                  desc='', title='', x_label='', y_label='', show_plot=True, filename=''):
        # fig, ax = plt.subplots()
        plt.plot(xdata, ydata)

        if title == '':
            title = self._title

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid()

        # fig.savefig("test.png")
        if filename != '':
            plt.savefig(filename)

        if show_plot:
            plt.show()

    def bar(self, xdata, ydata,
                 desc='', title='', x_label='', y_label='', show_plot=True, filename=''):

        plt.bar(xdata, ydata)

        if title == '':
            title = self._title

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid()

        # fig.savefig("test.png")
        if filename != '':
            plt.savefig(filename)

        if show_plot:
            plt.show()