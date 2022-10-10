# - Play with list operations listed on slide #6 of Part 1 (except "for" loop).
def play_with_lists():
  list_1=[1,2,3,4,]
  print(f"Partial list 1: {list_1}")
  list_2=[9,8,7,6,5]
  print(f"Partial list 2: {list_2}")
  list_2=list_2[::-1]
  full_list = [*list_1,  *list_2]
  print(f"full list: {full_list}")
  second_from_last = full_list[-2]
  print(f"Second from last item: {second_from_last}")

# - Play with split() and join() functions as in slides #17-18 of Part 1.
def split_join():
  example_csv = "column_1,column_2,column_3,column_4,column_5"
  csv_data = example_csv.split(",")
  example_tsv = "\t".join(csv_data)
  print(f"CSV: {example_csv}")
  print(f"TSV: {example_tsv}")

# - Play with all three flavors of the range() function as in slides #49-51 of Part 2.
def range_stuff():
  print("Range 0-8")
  print(list(range(8)))

  print("Range 0-8 with defined start point")
  print(list(range(0,8)))


  print("Range 0-20 with defined start point and step distance")
  print(list(range(0,20,3)))

# - Show use of "for" loop iterated over (i) string, (ii) list, and (iii) range(). Take different screenshots if needed.
def for_stuff():
  
  long_boi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

  long_str = "Pneumonoultramicroscopicsilicovolcanoconiosis"

  print("\nreversed str")
  for i in long_str[::-1]:
    print(f"{i} ", end="")

  print("\nEvery element")
  for i in long_boi:
    print(f"{i} ", end="")

  print("\nEvery other element")
  for i in range(0,len(long_boi)-1,2):
    print(f"{long_boi[i]} ", end="")


if __name__ == "__main__":
  play_with_lists()
  split_join()
  range_stuff()
  for_stuff()