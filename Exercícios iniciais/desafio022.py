name = input('Digite seu nome completo:').strip()

print(name.upper())
print(name.lower())
print(name.title())
print(len(name) - name.count(' '))
name1 = name.split()
print(len(name1[0]))
