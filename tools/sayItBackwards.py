def reverse(str):
	pm = ''
	if str[-1] in '!@#$%^&*()_+-=?/"\\}{[]<>,.|~`\'':
		pm = str[-1]
		str = str[0].lower() + str[1:-1]
	else:
		str = str[0].lower() + str[1:]

	old_list = str.split(' ')
	old_list[-1] = old_list[-1].capitalize()
	new_list = []
	length = len(old_list)

	for i in range(length):
		new_list.append(old_list[-(i+1)])

	return ' '.join(new_list) + pm

string = "How are You doing?"
print("\n"*10)
print("Enter a sentence and Simon will read it to you in backwards Like this!\n")
print(f"[Original] {string}")
print(f"[Reversed] {reverse(string)}\n")

while True:
	string = input(": ")
	print(f"Simon said '{reverse(string)}'\n")