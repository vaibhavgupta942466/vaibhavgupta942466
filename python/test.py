def count_evens(nums):
  # CODE GOES HERE
  even_count = 0
  for i in nums:
      if i%2 == 0:
          even_count = even_count + 1
  return even_count



x = count_evens([2,1,2,3,0])
print(x)