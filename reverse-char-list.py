# Write a function that takes a list of characters and reverses the letters in place

def reverse(list_of_chars):
    # Initialize two pointers, left_index and right_index, 
    # which point to the first and last characters of the list, respectively.

    # While loop that continues as long as the left pointer is less than the right pointer.
    while left_index < right_index:
      # Swap characters to reverse the order
      list_of_chars[left_index], list_of_chars[right_index] = list_of_chars[right_index], list_of_chars[left_index]
      
      
      # moves the left pointer one position to the right and the right pointer one position to the left,
      # bringing them closer to the middle of the list
      left_index  += 1
      right_index -= 1

      # The while loop continues until the left and right pointers meet in the middle of the list,
      # at which point the function has reversed the order of all the characters in the list

    