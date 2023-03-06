"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))

"""


def merge_lists_easy(my_list, alices_list):
    if len(my_list + alices_list) == 0:
        return []

    merged_list = sorted(my_list + alices_list)

    # (my_list + alices_list).sort()
    return merged_list


merge_lists_easy([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])


def merge_list_manual(my_list, alices_list):

  # allocate our answer list, getting its size by adding the size of my_list and alices_list.
  merged_list_size = len(my_list) + len(alices_list)

  # Initialize a list of total length of the 2 arrays with none
  merged_list = [None] * merged_list_size

  current_index_alices = 0
  current_index_mine = 0
  current_index_merged = 0

  # Loop through the merged list
  while current_index_merged < merged_list_size:
      is_my_list_exhausted = current_index_mine >= len(my_list)
      is_alices_list_exhausted = current_index_alices >= len(alices_list)
      if (not is_my_list_exhausted and
              (is_alices_list_exhausted or
                my_list[current_index_mine] < alices_list[current_index_alices])):
          # Case: next comes from my list
          # My list must not be exhausted, and EITHER:
          # 1) Alice's list IS exhausted, or
          # 2) the current element in my list is less
          #    than the current element in Alice's list
          merged_list[current_index_merged] = my_list[current_index_mine]
          current_index_mine += 1
      else:
          # Case: next comes from Alice's list
          merged_list[current_index_merged] = alices_list[current_index_alices]
          current_index_alices += 1

      current_index_merged += 1

  return merged_list

merge_list_manual([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])