# ------------------------------------------------------------
# 3. Python uses scopes to find names
# ------------------------------------------------------------
# When Python sees a name, it must decide.
# Where is this name defined?
# Python follows a fixed rule called LEGB.


# ------------------------------------------------------------
# 4. LEGB Rule (Search Order)
# ------------------------------------------------------------
# L. Local scope
#    Inside the current function
#
# E. Enclosing scope
#    Inside outer functions (nested functions)
#
# G. Global scope
#    At the file or module level
#
# B. Built-in scope
#    Python built-ins like print, len, range
