# ------------------------------------------------------------
# 12. nonlocal keyword
# ------------------------------------------------------------
# Used in nested functions.
# Allows changing a variable from the enclosing scope.

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)     # Output: 20