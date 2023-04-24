with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]


score_pedra = 1
score_papel = 2
score_tesoura = 3

win = 6
loss = 0
tie = 3

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

score_p1 = 0
score_p2 = 0
for batle in content:
    score_p1 += outSocore[batle]
    score_p2 += outSocore2[batle]
    
    


    
print(f'Score {score_p1}')
print(f'Score {score_p2}')

#player 1
# A = Rock = 1
# B = paper = 2
# C = scissor  = 3  

#player 2
#  X = Rock = 1
#  Y = paper = 2
#  Z = scissor = 3

# A VS X = tie (3 + 1) = 4
# A VS Y = win (6 + 1) = 7
# A VS Z = loss (0 + 1) = 1

# B VS X = loss (0 + 2) = 2
# B vs y = tie (3 + 2) = 5
# B VS Z = win (6+ 2) = 8

# C VS X = loss (3 + 0) = 3
# C VS Y = win  (3 + 6) = 9
# C VS Z = tie  (3 + 3) = 6