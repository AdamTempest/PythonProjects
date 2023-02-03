# In many jurisdictions a small deposit is added to drink containers 
# to encourage people to recycle them. In one particular jurisdiction, 
# drink containers holding one liter or less have a $0.10 deposit, and 
# drink containers holding more than one liter have a $0.25 deposit.

# Write a program that 
# 1. reads the number of containers of each size from the user.
# 2. Compute and display the refund that will be received for returning those containers. 
# 3. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

def tryInting(strnum, msg):
	try:
		strnum = int(strnum)
	except Exception:
		print("[x] Invalid Input. Please enter an integer.")
		strnum = input(msg)
		strnum = tryInting(strnum,msg)
	return strnum

msg = "Enter the number of containers that have one liter or less: "
one_liter = tryInting(input(msg),msg)

msg = "Enter the number of containers that have more than one liter: "
more_than_one_liter = tryInting(input(msg),msg)

refund = one_liter*0.10 + more_than_one_liter*0.25
print("You are refunded for ",refund,"$")