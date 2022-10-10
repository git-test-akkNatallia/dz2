# dict_telephone = {"key": "value"}
#
# def func(*args, **kwargs):
#     if key == args:
#         return kwargs
#     else:
#         return "Undefind"
# dict_telephone = {
#     "Ivan": "1265",
#     "Oleg": "4927",
#     "Vlad": "9820",
#     "Irina": "1223",
#     "Natalia": "4678",
#     "Vera": "2738",
#     "Maksim": "4738",
#     "Alina": "3637"
# }
#
# print(dict_telephone)
# for i in dict_telephone:
#     print(i)


# telephone_book = {
#     "Ivan": "1265",
#     "Oleg": "4927",
#     "Vlad": "9820",
#     "Irina": "1223",
#     "Natalia": "4678",
#     "Vera": "2738",
#     "Maksim": "4738",
#     "Alina": "3637"
# }
# for i in range(int(input())):
#     line = input().split()
#     if str[1] not in telephone_book:
#         telephone_book[str[1]] = [str[0]]
#     else:
#         telephone_book[str[1]].append(str[0])
# for i in range(int(input())):
#     print(*telephone_book.get(input()), (["undefind"]))




#
# contact = {}
#
#
# def display_contact():
#     print("Name\t\tContact Number")
#     for key in contact:
#         print("{}\t\t{}".format(key, contact.get(key)))
# while True:
#     choice = int(input(" 1.Add new contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact \n 5.Delete contact \n 6.Exit \n Enter your choice"))
#     if choice == 1:
#         name = input("enter the contact name")
#         phone = input("enter the mobile number")
#         contact[name] = phone
#     elif choice == 2:
#         search_name = input("enter the contact name")
#         if search_name in contact:
#             print(search_name, "s contact number is ", contact[search_name])
#         else:
#             print("Undefind")
#     elif choice ==3:
#         if not contact:
#             print("empty contact book")
#         else:
#             display_contact()
#     elif choice == 4:
#         edit_contact = input("Enter the contact to be edited")
#         if edit_contact in contact:
#             phone = input("enter mobile number")
#             contact[edit_contact] = phone
#             print("contact updated")
#             display_contact()
#         else:
#             print("Undefind")
#     elif choice == 5:
#         del_contact = input("Enter the contact to be deleted")
#         if del_contact in contact:
#             confirm = input("Do you want to delete this contact yes/no?")
#             if confirm == "yes" or confirm == "Y":
#                 contact.pop(del_contact)
#             display_contact()
#         else:
#             print("Undefind")
#     else:
#         break



# book = dict( Ivan=1265, Oleg=4927, Vlad=9820, Irina=1223, Natalia=4678,
# Vera=2738, Maksim=4738, Alina=3637)
#
# print(book)


# q = dict.fromkeys(['Natallia', 'Vera', 'Oleg', 'Vuka'], 2345)
# print(q)




def search():
    name = input('> ')
    if name in phone_book:
        return F'{name} {phone_book}'
    else:
        return"Undefinde"
with open("tmp.txt") as file:
    date = file.read().splitlines()
phone_book = {}
for line in date:
    name = list(filter(lambda x :
    number = line[line[len(name):]]))




#
#
# print("Enter name")
# with open ("tmp.txt", 'w') as file:
#
#     while True:
#         name = input("Name >")
#         if not name:
#             break
#         number = input("number(a) > ")
#         file.write(f"{name}{number}\n")
# file.close()

#     "Ivan": "1265",
#     "Oleg": "4927",
#     "Vlad": "9820",
#     "Irina": "1223",
#     "Natalia": "4678",
#     "Vera": "2738",
#     "Maksim": "4738",
#     "Alina": "3637"




# import warnings
# from typing import Union, Set, Any
#
# dictionary_phone = {"Pavel": 4567, "Alex": 3425, "Michel": 6243, "Maxim": 3456}
#
# def get_phone_number_1(dictionary: dict, name:str):Union[str,int]
#     return "undefinded" if dictionary.setdefault(name) is None else dictionary[name]
#
# print(get_phone_number_1(dictionary_phone, 'Jonh'))
# print(get_phone_number_1(dictionary_phone, 'Pavel'))
# print(get_phone_number_1(dictionary_phone, 'Alex'))

    # result = 'undefinded'
    # if dictionary.setdefault(name) is None
    # else dictionary[name]
    #     if len(str(result)) > 4 and result != "undefinded":
    #




