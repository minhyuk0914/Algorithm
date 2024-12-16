def solution(players, callings):
    players_dict = {player : idx for idx, player in enumerate(players)}
    
    for call in callings:
        swap_1 = players_dict[call]
        swap_2 = swap_1 - 1
        
        players[swap_1], players[swap_2] = players[swap_2], players[swap_1]
        players_dict[players[swap_1]] = swap_1
        players_dict[players[swap_2]] = swap_2

    return players