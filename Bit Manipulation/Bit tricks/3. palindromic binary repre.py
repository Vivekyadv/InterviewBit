# Given integer n, find nth number whose binary representation is palindrome
# Note: take 1 as first no whose bin rep is palindrome instead of 0

# Method from geeksforgeeks
# Link: https://www.geeksforgeeks.org/find-n-th-number-whose-binary-representation-palindrome/

INT_SIZE = 32

def constructNthNumber(group_no, aux_num, op):

	a = [0] * INT_SIZE
	num, i = 0, 0

	if op == 2:
		len_f = 2 * group_no
		a[len_f - 1] = a[0] = 1
		while aux_num:
			a[group_no + i] = a[group_no - 1 - i] = \
				aux_num & 1
			aux_num = aux_num >> 1
			i += 1

	elif op == 0:

		len_f = 2 * group_no + 1
		a[len_f - 1] = a[0] = 1
		a[group_no] = 0
		while aux_num:
			a[group_no + 1 + i] = a[group_no - 1 - i] = \
				aux_num & 1
			aux_num = aux_num >> 1
			i += 1

	else: 
		len_f = 2 * group_no + 1
		a[len_f - 1] = a[0] = 1
		a[group_no] = 1
		while aux_num:
			a[group_no + 1 + i] = a[group_no - 1 - i] = \
				aux_num & 1
			aux_num = aux_num >> 1
			i += 1

	for i in range(0, len_f):
		num += (1 << i) * a[i]
	return num

def getNthNumber(n):
	if n == 1:
		return 1
	group_no = 0
	count_upto_group, count_temp = 0, 1
	while count_temp < n:

		group_no += 1
		count_upto_group = count_temp
		count_temp += 3 * (1 << (group_no - 1))

	group_offset = n - count_upto_group - 1
	if (group_offset + 1) <= (1 << (group_no - 1)):

		op = 2 
		aux_num = group_offset

	else:

		if (((group_offset + 1) -
			(1 << (group_no - 1))) % 2):
			op = 0 
		else:
			op = 1 
		aux_num = (((group_offset) -
					(1 << (group_no - 1))) // 2)

	return constructNthNumber(group_no, aux_num, op)

print(getNthNumber(9))


# Method 2: find group no and offset in which given num lies 
# Video reference Link: https://www.youtube.com/watch?v=QYoWR8hDCyQ

def solve(n):
	count = len = 1
	while count < n:
		len += 1
		elementsOfLen = (1 << (len-1)//2)
		count += elementsOfLen
	count -= (1 << (len-1)//2)

	offset = n - count - 1
	ans = 1 << (len-1)
	ans |= (offset << (len//2))

	valFR = (ans >> (len//2))
	rev = getRev(valFR)

	ans |= rev
	return ans

def getRev(n):
	rev = 0
	while n != 0:
		lb = n & 1
		rev |= lb
		rev <<= 1
		n >>= 1
	rev >>= 1
	return rev 

print(solve(9))