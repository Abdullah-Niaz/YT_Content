# ------------------------------------------------------------
# 7. Global Scope
# ------------------------------------------------------------
# Variables created outside all functions are global.
# Functions can read global variables.
# Assignment creates local variables by default.

x = 100         # global variable

def show():
    print(x)    # reading global variable is allowed
