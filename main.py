def main():
   path_to_file = "books/frankenstein.txt"
   text = get_text_from_file(path_to_file).lower()
   count = word_count(text)
   dictionary = to_dictionary(text)
   sorted_dictionary = sort_dictionary(dictionary)

   print(f"=== Begin report of {path_to_file} ===")
   print(f"There are {count} words in the text.\n")

   for key, value in sorted_dictionary:
      if key.isalpha():
         print(f"The letter '{key}' appears {value} times.")
   print()

   print("=== End of report ===")

def sort_dictionary(dictionary):
   return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

def get_text_from_file(path):
   with open(path) as f:
      return f.read()

def word_count(text):
   return len(text.split())

def to_dictionary(text):
   words = text.split()
   dictionary = {}
   for word in words:
      for char in word:
         if char not in dictionary:
            dictionary[char] = 1
         else:
            dictionary[char] += 1
   return dictionary

if __name__ == "__main__":
   main()