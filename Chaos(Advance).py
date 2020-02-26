# (Advanced) Modify the chaos program so that it accepts two inputs and then prints a table with two columns similar to
# the one shown in Section 1.8. (Note: You will probably not be able to get the columns to line up as nicely as those
# in the example. Chapter 5 discusses how to print numbers with a fixed number of decimal places.)


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a number between 0 and 1: "))
    print("%-20s %-20s" % (x, y))
    print('---------------------------------')
    for i in range(10):
        x = 3.9 * (x - x * x)
        y = 3.9 * (y - y * y)
        print("%-20s %-20s" % (x, y))


main()
