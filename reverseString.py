# This can simply be done with one line:
# "reversed_string = string[:-1:-1].capitalize() + string[-1]"
#
# But I wanted it hard way, so here it is.

def reverseString(string):
	start = string[0].lower() # h
	end = string[-1] # d
	pm = ''
	puntuation_marks = '!@#$%^&*()_+-=?/"\\}{[]<>,.|~`\''

	if end in puntuation_marks:
		pm = end
		end = string[-2].upper()
		string = string[1:-2]
	else:
		end = end.upper() # D
		string = string[1:-1] # ello Go
	
	length = len(string)
	new_string = ''
	for i in range(length): # 7 # 1 # ello Go
		new_string += string[-(i+1)] # To Avoid -0

	return (end + new_string + start + pm)

while True:
	print("====       String Reversion Tool       ====")
	print("==                                       ==")
	print("==    Enter a string to reverse it.      ==")
	print("== Enter quit or press CTRL + C to exit. ==")
	print("===========================================\n")
	string = input("Enter: ")
	if string in ["Quit","quit"]:
		break
	print(reverseString(string))
	input()