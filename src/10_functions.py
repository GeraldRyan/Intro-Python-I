# Write a function is_even that will return true if the passed-in number is even.


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# YOUR CODE HERE
def is_even(num):
    if num%2==0:
      return True
    else:
      return False

def tell_me_even(num):
  if is_even(num):
    print("Even!")
  else:
    print("Odd")

tell_me_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

