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
    name1=""
    name1=f_name+" "+l_name
    print(f"your full name is {name1}")
first_name = input("Enter your first name ").lower()
last_name = input("Enter your last name ").lower()
name(first_name,last_name)#Write your code below this row