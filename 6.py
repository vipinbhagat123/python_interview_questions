# Import module
import threading

# create thread
t1 = threading.Thread(target, args)
t2 = threading.Thread(target, args)

# start thread

t1.start()
t2.start()

# to stop the program unit a thread is complete.
t1.join()
t2.join()


