import random
from string import ascii_letters, digits, punctuation

def rand_passwd(n, mode):
	if 4 <= n <= 256 and 0 <= mode <= 2:
		choice = {
			0: ascii_letters,
			1: ascii_letters + digits,
			2: ascii_letters + digits + punctuation
		}.get(mode)
		
		return "".join([random.choice(choice) for x in range(n)])
	else:
		print("ERROR. Input numbers in the correct range.")
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

print(f"""
{"-"*(string_length + 23)}
# Number of characters : {string_length}
# Mode : {string_mode}
# String : {rand_passwd(string_length, string_mode)}
{"-"*(string_length + 23)}
""")
