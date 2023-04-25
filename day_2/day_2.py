with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]


score_pedra = 1
score_papel = 2
score_tesoura = 3

win = 6
loss = 0
tie = 3

score_p1 = 0
score_p2 = 0

outSocore = {
    'A X': tie + score_pedra, 'A Y': win + score_papel , 'A Z': loss + score_tesoura,
    'B X': loss + score_pedra, 'B Y': tie + score_papel, 'B Z': win + score_tesoura,
    'C X': win + score_pedra, 'C Y': loss + score_papel, 'C Z': tie + score_tesoura 
}

outSocore2 = {
    'A X': loss + score_tesoura, 'A Y': tie + score_pedra , 'A Z': win + score_papel,
    'B X': loss + score_pedra, 'B Y': tie + score_papel, 'B Z': win + score_tesoura,
    'C X': loss + score_papel, 'C Y': tie + score_tesoura, 'C Z': win + score_pedra 
}


for batle in content:
    score_p1 += outSocore[batle]
    score_p2 += outSocore2[batle]
    
    
print(f'Score {score_p1}')
print(f'Score {score_p2}')

