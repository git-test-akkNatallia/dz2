homework_file = open('q4_urls.txt', 'r', encoding='utf-8')
_dict = {}
for _string in homework_file.readlines():
    if _string not in _dict:
        _dict[_string] = 0
    _dict[_string] += 1
homework_file.close()
new_file = open('sorted_string', 'w', encoding='utf-8')

for key, value in sorted(_dict.items(), key=lambda x: x[1], reverse=True):
    new_file.write(f'{value} {key}')
new_file.close()
print(new_file)

