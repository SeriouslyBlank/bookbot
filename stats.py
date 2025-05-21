def no_words(cnt):
	num_words = cnt.split()
	len_num = len(num_words)
	return len_num


def ch_dict(char):
	char_list = char.split()
	char_string = ''
	char_set = set()
	char_dict = {}
	for c in char_list:
		char_string += c 

	char_string = char_string.lower()

	for c in char_string:
		char_set.add(c)

	for c in char_set:
		count = 0
		for c2 in char_string:
			if c2 == c:
				count += 1
		char_dict[c] = count

	char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse = True))

	for c in char_dict:
		if not c.isalpha():
			pass
		else:
			print(f"{c}: {char_dict[c]}")



	