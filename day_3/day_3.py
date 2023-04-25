with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]

sum_score = 0
sum_score_group = 0

def pontuacao(letra):
    codigo = ord(letra)
    if codigo >= 97 and codigo <= 122:
        return codigo - 96
    elif codigo >= 65 and codigo <= 90:
        return codigo - 38
    else:
        return 0
    
for data in content:


    lenText = len(data)
    bag1 = data[:lenText//2]
    bag2 = data[lenText//2:]

    letras_repetidas = set()

    for letra in bag1:
        if letra in bag2 and letra not in letras_repetidas:
            letras_repetidas.add(letra)
            sum_score += pontuacao(letra)

print(sum_score)




grupos = [content[i:i+3] for i in range(0, len(content), 3)]

for i, grupo in enumerate(grupos, 1):
    print(f"Grupo {i} >>>>>>>>>>")
    letras1 = set(grupo[0])
    letras2 = set(grupo[1])
    letras3 = set(grupo[2])
    letras_repetidas = letras1.intersection(letras2, letras3)
    if len(letras_repetidas) > 0:
        print(letras_repetidas)
        score = 0
        for letra in letras_repetidas:
            score += pontuacao(letra)
        sum_score_group += score
       
        
        
print(sum_score_group)

#cada mochila tem dois compartimentos
#cada linha é uma mochila