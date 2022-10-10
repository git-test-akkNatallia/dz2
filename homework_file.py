# t_file = open("q4_urls.txt", 'r', encoding='utf-8')
# my_dict = {}
#
# for num, line in enumerate(t_file, 1):
#     if "Davidson" in line:
#         print("№" + str(num) + ":" + line.strip())
#
# t_file.close()



# if line not in my_dict:
    #     my_dict[i] = 0

new_file = open("tmp.txt", "r", encoding='latin_1')
name_tolookfor = "Vera"
sq_file = open("red.txt", "w", encoding='latin_1')
for num, line in enumerate(new_file):
    if name_tolookfor in line:
        print("Line №:" + ":" + line)
        sq_file.write("Name:" + line)

new_file.close()
sq_file.close()









