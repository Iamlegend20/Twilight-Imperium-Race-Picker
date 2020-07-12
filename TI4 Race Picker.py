import random

class Player:
    def __init__(self, name):
        self.name = name
        self.choices = []
        self.race = None
    def __repr__(self):
        return self.name
    def show_choices(self):
        print(f'{self.choices[0]} or {self.choices[1]}')
    def show_numbered_choices(self):
        print(f'1.{self.choices[0]} or 2.{self.choices[1]}')
    def show_race(self):
        print(f'{self.name} is the {self.race}')
    
def get_player_names():
    names = []
    while True:
        givenname = input('Enter name. Leave blank if finished.')
        if givenname:
            names.append(givenname.capitalize())
        else:
            return names

def display_races(races):
    for number,race in enumerate(races, 1):
        print(f'{number}. {race}')

def display_players(players):
    for number,player in enumerate(players, 1):
        print(f'{number}. {player}')
        
def get_user_choice(num_options):
    while True:
        user_choice = input().lower()
        if user_choice.isdecimal() and int(user_choice)-1 in range(num_options):
            return int(user_choice)-1
        elif user_choice == '':
            return None
        print("That's not a valid input.")

def ban_races():
    races = ['The Universities of Jol-Nar', 'The Federation of Sol', 'The Clan of Saar', 'The Naalu Collective', 'The Emirates of Hacan', 'The Yssaril Tribes', 'The Winnu', 'The L1Z1X Mindnet', 'The Barony of Letnev', 'The Mentak Coalition', 'The Yin Brotherhood',  'The Ghosts of Creuss', 'The Nekro Virus', 'The Arborec', 'The Xxcha Kingdom', 'The Embers of Muaat', 'The Sardakk N’orr']
    while True:
        display_races(races)
        print('Choose a race to ban. Leave blank if finished.')
        user_choice = get_user_choice(len(races))
        if user_choice == None:
            return races
        else:
            races.pop(user_choice)

def create_players(names):
    players = []
    for name in names:
        players.append(Player(name))
    random.shuffle(players)
    print('\nThe players have been randomly shuffled.')
    display_players(players)
    input('Press Enter to continue.\n')
    return players    

def deal_first_race(players, upper_tier_races):
    random.shuffle(upper_tier_races)
    for player in players:
        random_race = upper_tier_races.pop()
        player.choices.append(random_race)
                                                
def deal_second_race(players, lower_tier_races):
    random.shuffle(lower_tier_races)
    index = 0
    for x in range(len(players)-1):
        random_race = lower_tier_races.pop()
        players[index].choices.append(random_race)
        index += 1
    print('The players have been randomly provided one race from the upper tier of races and one race from the lower tier of races.\n'
          f'{players[-1]} has only been provided a race from the upper tier of races. His lower tier race will be provided from the unchosen races of the other players.')
    input('Press Enter to continue.\n')

def show_player_choices(players):
    index = 0
    for x in range(len(players)-1):
        print(f'{players[index].name}:')
        players[index].show_choices()
        index += 1
    print('\n')

def choose_races(players, lower_tier_races, last_player=False):
    index = 0
    a = 1
    if last_player:
        a = 0
    for x in range(len(players) - a):
        current_player = players[index]
        print(f'{current_player.name} please select a race.')
        current_player.show_numbered_choices() 
        user_choice = get_user_choice(len(current_player.choices))
        current_player.race = current_player.choices[user_choice]
        print(f'{current_player.name} has selected {current_player.race}!')
        unchosen_race = current_player.choices.pop(user_choice-1)
        lower_tier_races.append(unchosen_race)
        print(f'{unchosen_race} has been returned to the pool of lower tier of races.')
        input('Press Enter to continue\n')
        index += 1
        
def last_player_choose(lower_tier_races, players):
        random.shuffle(lower_tier_races)
        random_race = lower_tier_races.pop()
        last_player = players[-1]
        last_player.choices.append(random_race)
        print(f'{last_player.name} has been provided his second race from the unchosen races of the other players.')
        input('Press Enter to continue.\n')
        choose_races([players[-1]],lower_tier_races, last_player=True)        
        
def announce_results(players):
    for player in players:
        player.show_race()
    
def determine_neighbors(players):
    print('The players will now be randomly shuffled to determine final seating order and neighbors.')
    input('Press Enter to continue.\n')
    random.shuffle(players)
    for player in players:
        player.show_race()
    print('\nMay the strongest race emerge victorious!...\nMe')

def main():
    names = get_player_names()
    players = create_players(names)
    races = ban_races()
    upper_tier_races = races[:6]
    lower_tier_races = races[6:]
    deal_first_race(players, upper_tier_races)
    deal_second_race(players, lower_tier_races)
    show_player_choices(players)
    choose_races(players,lower_tier_races)
    last_player_choose(lower_tier_races,players)
    determine_neighbors(players)

if __name__ == '__main__':
    main()
