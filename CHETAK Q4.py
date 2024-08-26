import numpy as np
import pandas as pd
import numpy as np
from scipy.stats import norm
import scipy as stats
import seaborn as sns
import random
import heapq

data_normal = norm.rvs(size=10000,loc=0, scale=0.75)
ax = sns.distplot(data_normal, bins=100, kde=True, color='skyblue', hist_kws = {"linewidth": 15, 'alpha':1})

ax.set(xlabel='Normal Distribution', ylabel='Frequency')

pdf = norm.pdf(data_normal, loc=0, scale=0.75)
pdff = pdf/np.sum(pdf)
random_output= np.random.choice (a= data_normal, p=pdff)
speed_ratio = 4**((np.random.choice(a= data_normal, p=pdff))/2)

player1= 1 #user's robot
player2= 2 #opponent's robot

class silogame:
    
    def __init__(self, number_of_silos , capacity_per_silo):
        self.number_of_silo= number_of_silos
        self.capacity_per_silo = capacity_per_silo
        self.silos = [[0]*capacity_per_silo for _ in range (number_of_silos)]       

    def display_silos(self):
        for rows in self.silos:
            print(rows)
        print()
    
    def insert_paddy(self, player, silo):
        if 1 <= silo <= self.number_of_silo :
            for i in range(self.capacity_per_silo):
                if self.silos[silo-1][i]== 0 :
                    self.silos[silo-1][i] = player
                    break
                if self.silos[silo-1].count(0) == 0:
                    print("the specifies silo has no vacancy")
                    break
                else:
                    print("the specifies silo is not in the range")
                    break
    
    def game_over(self):
        for rows in self.silos:
            if rows.count[0] != 0:
                return True
            else:
                return False
            
    def game_win(self , player):
        for rows in self.silos:
            if rows.count[player] >= 2 and rows[-1] == player:
                win_list=[]
                rows.append(win_list)
                if len(win_list) == 3 :
                    print(f"Player {player} won the match")
                    self.display_silos()
                    return True
            else:
                self.game_over()
                print("Its a draw")
                return True

    #Smart move - 1        
    def blocking_silo(self, player):
        for index , silo in enumerate(self.silos, start = 1):
            if silo.count[player] == 2 and silo[-1] == 0:
                return index
            else: 
                return True

    #Smart Move - 2
    def winning_silo(self, player):
        for index , silo in enumerate(self.silos, start = 1):
            if silo.count[player] >= 1 and silo[-1] == 0:
                return index

    #integrating both the Smart Moves
    def smart_moves(self, player):
        winning_silo = self.winning_silo(player)
        if winning_silo is True:
            return winning_silo

        blocking_silo = self.blocking_silo(player)
        if blocking_silo is True:
            return blocking_silo

    def random_move(self):
        for index , silo in enumerate(self.silos, start = 1):
                if silo[-1] == 0:
                    random = random.choice(index)
                    return random
                return None
    
    def player(self, speed_ratio):
        # Define events with their times and players
        events = [(0, player1), (0, player2)]

        heapq.heapify(events)

        # Simulate the game
        while True:
            self.display_silos()

            time, player = heapq.heappop(events)
            if player == player1:
                silo = self.smart_moves(player)
            else: #opponent's robot
                silo = self.random_move()
            if silo is None:
                print(f"Player{player} takes a turn at time {time}")

            self.insert_paddy(player,silo)
            if self.game_win :
                break

            new_time = time + 1  # Assuming each turn takes 1 unit of time
            heapq.heappush(events, (new_time, player))
if __name__== "_main_":
    game = silogame(num_silos=5, capacity_per_silo=3)
    game.play(speed_ratio)







