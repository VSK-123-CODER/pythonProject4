#Write your code below this line 👇
def name(first_name,last_name):
  f_name = ""
  for i in range(0, len(first_name)):
    if i == 0:
      f_name += first_name[0].upper()
      i += 1
      continue
    f_name += first_name[i]

  l_name = ""
  for i in range(0, len(last_name)):
    if i == 0:
      l_name += last_name[0].upper()
      i += 1
      continue
    l_name += last_name[i]
  print(f_name+" "+l_name)

