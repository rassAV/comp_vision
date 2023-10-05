names = ["figure1.txt", "figure2.txt", "figure3.txt", "figure4.txt", "figure5.txt", "figure6.txt"]
print("Номинальные разрешения (мм/пиксель):")
for name in names:
  file = open(name, "r")
  n = float(file.readline()[:-1])
  max_len = 0
  for l in file:
    symbols = l.split()
    length = 0
    for s in symbols:
      if s == "1":
        length += 1
    if max_len < length:
      max_len = length
  nom_res = max_len / n
  if nom_res == 0:
    print(name, "\t нет изображения \n")
  else:
    print(name, "\t", max_len / n, "\n")

names = ["img1.txt", "img2.txt"]
file1 = open(names[0], "r")
y1 = 0
x1 = 0
for i, line in enumerate(file1):
  line = line.split()
  for j, l in enumerate(line):
    if l == "1":
      y1 = i
      x1 = j
      break
file2 = open(names[1], "r")
y2 = 0
x2 = 0
for i, line in enumerate(file2):
  line = line.split()
  for j, l in enumerate(line):
    if l == "1":
      y2 = i
      x2 = j
      break
print("Смещение изображения:")
print("y = ", abs(y1 - y2), "\t x =", abs(x1 - x2))
