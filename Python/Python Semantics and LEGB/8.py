# ------------------------------------------------------------
# 9. LEGB Example
# ------------------------------------------------------------
x = 1


def outer():
    x = 2

    def inner():
        print(x)   # Python finds x in enclosing scope
    inner()


outer()   # Output: 2
