s = 'camelCasingCodingStyle'
new_s = []

for item in s:
    if item.isupper():
        new_s.append(' ')
    new_s.append(item)
new_s = ''.join(new_s).lstrip()

print(new_s)

