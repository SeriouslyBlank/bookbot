from stats import no_words, ch_dict

def get_book_text(path_to_file):
	with open(path_to_file,encoding='utf-8') as f:
		file_contents = f.read()
		return file_contents

def main():
	content = get_book_text("books/frankenstein.txt")
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	wc = no_words(content)
	print("----------- Word Count ----------")
	print(f"Found {wc} total words")
	print("--------- Character Count -------")
	ch_dict(content)
	print("============= END ===============")


main()
