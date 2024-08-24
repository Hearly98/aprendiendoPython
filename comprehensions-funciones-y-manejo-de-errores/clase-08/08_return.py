def sum_with_range(min, max):
  print(min, max)
  sum = 0
  for x in range(min, max):
    sum += x
  return sum


sum_with_range(1, 20)

#Si queremos guardar los datos
result = sum_with_range(1, 20)
print(result)

result_2 = sum_with_range(result, result + 10)
print(result_2)
