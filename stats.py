def get_num_words(text):
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

def sort_on(item):
   return item["num"]

def dict_to_sorted_list(dictionary):
   sorted_list = []
   for ch in dictionary:
      sorted_list.append({"char": ch, "num": dictionary[ch]})
   sorted_list.sort(key=sort_on, reverse=True)
   return sorted_list
