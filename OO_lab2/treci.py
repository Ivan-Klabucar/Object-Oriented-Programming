def mymax(iterable, key=lambda x: x):
  # incijaliziraj maksimalni element i maksimalni ključ
  max_x = max_key = None

  # obiđi sve elemente
  for x in iterable:
    if not max_x or key(x) > max_key:
        max_key = key(x)
        max_x = x

  # vrati rezultat
  return max_x


maxint = mymax([1, 3, 5, 7, 4, 6, 9, 2, 0])
maxchar = mymax("Suncana strana ulice")
maxstring = mymax([
  "Gle", "malu", "vocku", "poslije", "kise",
  "Puna", "je", "kapi", "pa", "ih", "njise"])


D={'burek':8, 'buhtla':5}
max_price = mymax(D, key=D.get)

names = [('ivana', 'zizela'), ('marko', 'rak'), ('zvone', 'zec')]
max_name = mymax(names)

print(f'maxint: {maxint}')
print(f'maxchar: {maxchar}')
print(f'maxstring: {maxstring}')
print(f'max_price: {max_price}')
print(f'max_name: {max_name}')