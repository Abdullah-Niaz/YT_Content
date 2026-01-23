# ------------------------------------------------------------
# 6. Enclosing Scope
# ------------------------------------------------------------
# Happens when a function is inside another function.
# Inner functions can read variables from outer functions.

def outer():
    x = 10       # enclosing variable

    def inner():
        print(x)  # Python finds x in enclosing scope
    inner()
