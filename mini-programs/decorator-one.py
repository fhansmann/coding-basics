def function_making_function(old_function):
  print("making a new function from", old_function)
  def new_function():
    print("calling the old function")
    old_function()
    print("done calling the old function")
  print("made the new function")
  return new_function
  
def some_function():
  print("in some_function")

print("starting to make a new function")
new_function = function_making_function(some_function) # not calling it here, just moving at around (remember, functions are objects!)
print("done making the new function")

print("calling the new function")
new_function()
print("done")

***
Output:

starting to make a new function
making a new function from <function old_function at 0xhesyfyua>
made the new function
done making the new function
calling the new function
calling the old function
in some_function
done calling the old function
done

***


# Decorator Syntax:

print("starting to make a new function")
@function_making_function
def some_function():
  print("in some_function")
print("done making the new function")

print("calling the new function")
some_function()
print("done")
