names="balaji srinivasan"
vowels="aeiou"
result=[char for char in names if not char in vowels]
print(result)
result=[char for char in names if char in vowels]
print(result)
print(names[0:16:3])
print(names[::-3])
print(names[:])
print(names[::2])
sep='-'.join(names[::2])
print(sep)

