letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
exclude = 'l'
for i in letters:
    if i == 'l': continue
    print(i)


sky_is = input('Write a sentence')
books = 'wW'
s = 0
for i in sky_is:
    if i in books:
        s +=1
print(s)

sky_in = input('Write a sentence')
book = 'w'
s1 = 0
for i in sky_in:
    if i in book:
        s1 +=1
print(s1)







