# count_lines = {}
# for line in open(r'tmp.txt'):
#     clean_line = line.rstrip()
#     if clean_line not in count_lines:
#         count_lines [line.strip()] = 0
#     count_lines[line.strip()] += 1

# count_lines = {}
# for line in open(r'tmp.txt'):
#     clean_line = line.rstrip()
#     if clean_line not in count_lines:
#         count_lines [clean_line] = 0
#     count_lines[clean_line] += 1
# out = open(r'new.txt', 'w')
# for line in open(r'tmp.txt'):
#     count = count_lines[line.rstrip()]
#     out.write(f'{line}; {count}')

l = [str(i) + str(i-1) for i in range(20)]
print(l)
f = open('tmp.txt', 'w')
for index in l:
    f.write(index + '\n')
f.close()
f = open('tmp.txt', 'r')
l = [line.strip() for line in f]
f.close()