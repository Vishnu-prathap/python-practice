# Python3 program for the above approach

# Function to print the result of the
# summation of numbers having K-digit
def printResult(result):

	# Reverse the array to
	# obtain the result
	result = result[::-1]

	i = 0
	while (i < len(result)):

		# Print every digit
		# of the answer
		print(result[i], end = "")
		i += 1

# Function to calculate the total sum
def sumOfLargeNumbers(v, k, N):
    # return sum(array) also works beautifully

	# Stores the array of large
	# numbers in integer format
	x = [[] for i in range(1000)]

	for i in range(k):
		for j in range(N):

			# Convert each element
			# from character to integer
			x[i].append(ord(v[i][j]) - ord('0'))

	# Stores the carry
	carry = 0

	# Stores the result
	# of summation
	result = []

	for i in range(N - 1, -1, -1):

		# Initialize the sum
		sum = 0

		for j in range(k):

			# Calculate sum
			sum += x[j][i]

		# Update the sum by adding
		# existing carry
		sum += carry
		temp = sum

		# Store the number of digits
		count = 0
		while (temp > 9):
			temp = temp % 10

			# Increase count of digits
			count += 1

		l = pow(10, count)
		if (l != 1):

			# If the number exceeds 9,
			# Store the unit digit in carry
			carry = sum / l

		# Store the rest of the sum
		sum = sum % 10

		# Append digit by digit
		# into result array
		result.append(sum)

	while (carry != 0):
		a = carry % 10

		# Append result until
		# carry is 0
		result.append(a)
		carry = carry // 10

	# Print the result
	printResult(result)

# Driver Code
if __name__ == '__main__':
	
	K = 10
	N = 5

	# Given N array of large numbers
	arr= [ "1111111111", "1111111111",
		"1111111111", "1111111111",
		"1111111111" ]

	sumOfLargeNumbers(arr, N, K)

# This code is contributed by mohit kumar 29
