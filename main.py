from stats import no_words, ch_dict
import sys

def get_book_text(path_to_file):
	with open(path_to_file,encoding='utf-8') as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) >= 2:
		file_path = sys.argv[1]
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	content = get_book_text(file_path)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {file_path}...")
	wc = no_words(content)
	print("----------- Word Count ----------")
	print(f"Found {wc} total words")
	print("--------- Character Count -------")
	ch_dict(content)
	print("============= END ===============")


main()
