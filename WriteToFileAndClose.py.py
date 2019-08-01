# run program, add .txt file name as argument
# import is a feature from feature libary
# argv argument variable can be used to pass data into the script
from sys import argv
script, filename = argv

# line 8 unpacks argv variable filename
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

# collect input from user, shows blink "?" for user to enter data
input("?")

print("opening the file...")
target = open(filename, 'w')

# truncates all text in the .txt file called from the argv
print("Truncating the file. Goodbye!")
target.truncate()

# requires user to input data, then saves input to .txt file
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# this closes the file
print("And finally, we close it.")
target.close()



