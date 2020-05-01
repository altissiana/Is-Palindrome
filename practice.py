# O(1) space | O(n) time
def isPalindrome(string):
    start = 0
	end = len(string) - 1
	while start <= end:
		if string[start] != string[end]:
			return False
		start = start + 1
		end = end - 1	
	return True
