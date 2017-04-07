def comparison_string(string_A, string_B):
	
	if string_A == string_B:
		return 1
	elif string_A != string_B and len(string_A) > len(string_B):
		return 2
	elif string_A != string_B and string_B == "learn":
		return 3

print(comparison_string('25656','learn'))

