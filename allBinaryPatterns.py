# Recursive Python program to generate all
# binary strings formed by replacing
# each wildcard character by 0 or 1

# Recursive function to generate all binary
# strings formed by replacing each wildcard
# character by 0 or 1
def _print(string, index):
	if index == len(string):
		print(''.join(string))
		return

	if string[index] == "?":

		# replace '?' by '0' and recurse
		string[index] = '0'
		_print(string, index + 1)

		# replace '?' by '1' and recurse
		string[index] = '1'
		_print(string, index + 1)

		# NOTE: Need to backtrack as string
		# is passed by reference to the
		# function
		string[index] = '?'
	else:
		_print(string, index + 1)

# Driver code
if __name__ == "__main__":

	string = "1??0?101"
	string = list(string)
	_print(string, 0)

	# This code is contributed by
	# sanjeev2552

# Note: function name _print is used because
# print is already a predefined function in Python

