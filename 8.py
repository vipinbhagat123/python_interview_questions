import threading
import time

def walk_dog():
    time.sleep(5)
    print("You finish walking the dog")

def tak_out_trash():
    time.sleep(3)
    print("You take out the trash")

def get_mail():
    time.sleep(7)
    print("You get the mail")

walk_dog()
tak_out_trash()
get_mail()


# Multithreading  = it is used to perform multiple tasks concurrently ( multitasking)
                  #Good for I/O bound tasks like reading files or fecting data from APIs

