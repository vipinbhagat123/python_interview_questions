import threading

def print_cube(number):
    print("Cube: {}" .format(number * number * number))

def print_square(number):
    print("Square:{}" .format(number * number))


if __name__ == '__main__':
    t1 = threading.Thread(target = print_square, args=(10,))
    t2 = threading.Thread(target = print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done!")
