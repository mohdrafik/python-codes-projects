import random
# def play(player, opponent):
def play():
    userinput = input("enter your choice:'r' for rock,'p' for paper's' for scissor:")
    computer = random.choice(['r','p','s'])
    # r>s, p>r, s>p 
    if userinput == computer:
        # print ("It\ a tie")
        return f'It\ a tie because computer also chooses {computer}'
    if if_win_palyer1(userinput,computer):
        return f'You won!!! beacuse computer chooses {computer}'
    
    return f'You lost!!! because computer chooses {computer}'


def if_win_palyer1(player1,player2):
    if (player1 == 'r' and player2 =='s') or (player1 == 'p' and player2 =='r') \
        or (player1 == 's' and player2 =='p'):
        return True

print(play())
        
    




