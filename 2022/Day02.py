from test import test

# Star 1
"""
Notes:
    Goal is to sum up total score
    Scoring Sum:
        Round W/L/T + Play Type
        A Rock Respose X 1
        B Paper Response Y 2 
        C Scissors Response Z 3
        Win 6 Loss 1 Draw 3  
"""
draw_cond = {"A" : "X", "B" : "Y", "C" : "Z"}
win_cond = {"A" : "Y", "B" : "Z", "C" : "X"}
loss_cond = {"A" : "Z", "B" : "X", "C" : "Y"}
round_score = {"win" : 6, "loss" : 0, "draw" : 3 }
play_score = {"X" : 1, "Y" : 2, "Z" : 3}
res = 0

for line in test.splitlines():
    game = line.split()
    
    if win_cond[game[0]] == game[1]:
        res += round_score["win"]
    elif draw_cond[game[0]] == game[1]:
        res += round_score["draw"]
    else:
        res += round_score["loss"]
    
    res += play_score[game[1]]

print("Star 1: ", res)
    
# Star 2
"""
Notes:
    Now 
"""

res = 0

for line in test.splitlines():
    game = line.split()
    
    # win 
    if game[1] == "X":
        res += round_score["loss"] + play_score[loss_cond[game[0]]]
    elif game[1] == "Y":
        res += round_score["draw"] + play_score[draw_cond[game[0]]]
    else:
        res += round_score["win"] + play_score[win_cond[game[0]]]
                                                                                               
print("Star 2: ", res)

