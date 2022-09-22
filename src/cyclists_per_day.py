#!/usr/bin/env python3

from numpy.core.numeric import outer
import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    pass

def split_date_continues():
    pass

def cyclists_per_day():
    pass

def main():
    a = cyclists_per_day()
    b = a.loc[(2017, 8), :]
    b.plot()
    plt.show()

if __name__ == "__main__":
    main()
