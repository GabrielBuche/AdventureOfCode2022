
with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]
    
count = 0
data = []

for item in content:
    if item == '':
        data.append(count)
        count = 0
    else:
        num = int(item)
        count += num
    
data_ordenada = sorted(data, reverse=True)

sum = data_ordenada[0] + data_ordenada[1] + data_ordenada[2]

print(f"O primeiro doende com mais calorias possui: {data_ordenada[0]} calorias.")
print(f"O segundo doende com mais calorias possui: {data_ordenada[1]} calorias.")
print(f"O terceiro doende com mais calorias possui: {data_ordenada[2]} calorias.")
print(f'No total eles carregam juntos: {sum} calorias.')