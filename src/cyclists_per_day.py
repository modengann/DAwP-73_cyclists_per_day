#!/usr/bin/env python3

from numpy.core.numeric import outer
import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    pass

def split_date_continues():
    # reading data from csv
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=";")

    # dropping unecessary rows and columns
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    # extracting first column to separate var
    col = df.iloc[:, 0]
    df = df.drop(df.columns[0], axis=1)

    # splitting data, translating
    col = col.str.split(expand=True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    col['Hour'] = col['Hour'].str[0:2]

    weekdays = {
        "ma": "Mon",
        "ti": "Tue",
        "ke": "Wed",
        "to": "Thu",
        "pe": "Fri",
        "la": "Sat",
        "su": "Sun"
    }

    months = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    col["Weekday"] = col["Weekday"].map(weekdays)
    col["Month"] = col["Month"].map(months)
    col = col.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    res = pd.concat([col, df], axis=1)

    return res

def cyclists_per_day():
    pass

def main():
    a = cyclists_per_day()
    b = a.loc[(2017, 8), :]
    b.plot()
    plt.show()

if __name__ == "__main__":
    main()
