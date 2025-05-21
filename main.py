from stats import no_words, no_chr

def get_book_text(path_to_file):
	with open(path_to_file,encoding='utf-8') as f:
		file_contents = f.read()
		return file_contents

def main():
	content = get_book_text("books/frankenstein.txt")
	wc = no_words(content)

	print(f"{wc} words found in the document")

	no_chr(content)


main()
