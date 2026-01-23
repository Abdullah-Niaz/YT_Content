# ------------------------------------------------------------
# 10. Reading vs Assignment (VERY IMPORTANT)
# ------------------------------------------------------------
# Reading a variable follows LEGB.
# Assigning a variable creates a LOCAL variable by default.

x = 10


def test():
    x = 5        # new local variable
    print(x)


test()
print(x)         # global x is unchanged
