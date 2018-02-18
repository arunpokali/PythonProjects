t=int(input())
assert 100 >= t >= 1
a=set(input())
print(a)
for _ in range(t-1):
  b=set(input())
  print(b)
  a = a.intersection(b)
  print(a)
print(len(a))