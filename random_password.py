import random
import string

def rand_str(n, mode):
	if 4 <= n <= 256 and 0 <= mode <= 2:

		if mode == 0:
			choice = string.ascii_letters
		elif mode == 1:
			choice = string.ascii_letters + string.digits
		elif mode == 2:
			choice = string.ascii_letters + string.digits + string.punctuation
		
		return "".join([random.choice(choice) for n in range(n)])
	else:
		print("ERROR. PLEASE TRY AGAIN.")
		import sys
		sys.exit(1)

try:
	string_length = int(input("Choose a positive integer n where 4 <= n <= 256: "))
	string_mode = int(input("Choose a mode (0 is all letters. 1 is letters and numbers. 2 is letters, numbers and punctuation characters): "))
except ValueError:
	print("ERROR. PLEASE TRY AGAIN.")
	input() # To let the user see the error message
	# Then exit the program
	import sys
	sys.exit(1)

string = rand_str(string_length, string_mode)

print(f"""
{"-"*(string_length + 25)}
# Number of characters : {string_length}
# Mode : {string_mode}
# String : {string}
{"-"*(string_length + 25)}
"""
)
