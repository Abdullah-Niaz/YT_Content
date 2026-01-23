# ------------------------------------------------------------
# 11. global keyword
# ------------------------------------------------------------
# Used when we want to change a global variable inside a function.

x = 10


def change():
    global x
    x = 20       # now changes global x
