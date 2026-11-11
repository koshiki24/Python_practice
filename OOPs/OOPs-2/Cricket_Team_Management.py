'''15. Cricket Team Management
Problem

Create player management system.

Requirements

Each player:

name
role
runs scored
Functionalities
Update runs
Display statistics
Maintain total players
Additional Challenge

Find highest scorer among all players.'''

class Player:
    total_players = 0
    player_object = []
    def __init__(self,name,role,runs_scored):
        self.__name = name
        self.__role = role
        self.__runs_scored = runs_scored
        Player.total_players += 1
        Player.player_object.append(self)

    def update_run(self,runs):
        self.__runs_scored += runs
        print("Runs updated successfully!")

    def display_statistics(self):
        print("--------------------Player Details--------------------")
        print(f"Player's Name : {self.__name}\nPlayer's Role : {self.__role}\nPlayer's Runs Scored : {self.__runs_scored}")

    @classmethod
    def display_total_players(cls):
        print(f"Total Player's are : {cls.total_players}")

    @classmethod
    def display_all_players(cls):
        for player in cls.player_object:
            player.display_statistics()
            print("-----------------------------")

    @classmethod
    def highest_scorer(cls):
        if len(cls.player_object) == 0:
            print("No Player Available")
        else:
            highest = cls.player_object[0]

            for player in cls.player_object:
                if player.__runs_scored > highest.__runs_scored:
                    highest = player

            print("Highest Scorer :")
            highest.display_statistics()

p1 = Player("Virat", "Batsman", 85)
p2 = Player("Rohit", "Batsman", 120)
p3 = Player("Bumrah", "Bowler", 45)


print("\nAll Player Statistics")
Player.display_all_players()


print("\nUpdating Runs")
p1.update_run(30)


print("\nUpdated Statistics")
p1.display_statistics()


print("\nTotal Players")
Player.display_total_players()


print("\nHighest Scorer")
Player.highest_scorer()


