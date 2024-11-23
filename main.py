def main():
   path_to_file = "books/frankenstein.txt"
   text = get_text_from_file(path_to_file)
   print(text)

def get_text_from_file(path):
   with open(path) as f:
      return f.read()

if __name__ == "__main__":
   main()