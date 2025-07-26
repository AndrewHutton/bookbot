# def main():
#    path_to_file = "books/frankenstein.txt"
#    text = get_text_from_file(path_to_file).lower()
#    count = word_count(text)
#    dictionary = to_dictionary(text)
#    sorted_dictionary = sort_dictionary(dictionary)



import sys
from stats import get_num_words, to_dictionary, dict_to_sorted_list

def main():
   if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
   path_to_file = sys.argv[1]
   text = get_book_text(path_to_file)
   num_words = get_num_words(text)
   dictionary = to_dictionary(text.lower())
   sorted_dict = dict_to_sorted_list(dictionary)
   print_report(path_to_file, num_words, sorted_dict)


def print_report(path_to_file, num_words, sorted_dict):
   print(f"============= BOOKBOT =============")
   print(f"Analysing book found at {path_to_file}...")
   print(f"----------- Word Count -----------")
   print(f"Found {num_words} total words")
   print(f"----------- Character Count -----------")   
   for item in sorted_dict:
      if item["char"].isalpha():
         print(f"{item['char']}: {item['num']}")
   print("============= End =============")

def get_book_text(path_to_file):
   with open(path_to_file) as f:
       return f.read()
   

if __name__ == "__main__":
    main()