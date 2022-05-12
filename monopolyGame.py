
# monopoly game without gui
class PlayerMonopoly:
    def __init__(self, name,  pcash, letter):
        self.name = name
        self.pcash = pcash
        self.letter = letter
        self.passets = []


class Monopoly:
    def __init__(self):
        # assets [[property name, if one property, charge this rent]]
        self.assets = [['Mediterranean Ave', 1, -10, 2, -30, 3, -90, 4, -160, 'Shop', -250, 'Mortgage value', -30, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Baltic Avenue', 1, -20, 2, -60, 3, -1800, 4, -3200, 'Shop', -450, 'Mortgage value', -30, 'House cost', -50, 'Shop cost', '50 and 4 houses'],
                       ['Oriental Avenue', 1, -30, 2, -90, 3, -270, 4, -400, 'Shop', -550, 'Mortgage value', -50, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Vermont Avenue', 1, -30, 2, -90, 3, -270, 4, -400, 'Shop', -550, 'Mortgage value', -50, 'House cost', -50, 'Shop cost', '50 and 4 houses'], ['Vermont Avenue', 1, -40, 2, -100, 3, -300, 4, -450, 'Shop', -600, 'Mortgage value', -60, 'House cost', -50, 'Shop cost', '50 and 4 houses'],
                       ['St Charles Place', 1, -50, 2, -150, 3, -450, 4, -625, 'Shop', -750, 'Mortgage value', -70, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['State Avenue', 1, -50, 2, -150, 3, -450, 4, -625, 'Shop', -750, 'Mortgage value', -70, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['Virginia Avenue', 1, -60, 2, -80, 3, -500, 4, -700, 'Shop', -900, 'Mortgage value', -80, 'House cost', -100, 'Shop cost', '100 and 4 houses'],
                       ['St James Palace', 1, -70, 2, -200, 3, -550, 4, -750, 'Shop', -950, 'Mortgage value', -90, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['Tennessee Avenue', 1, -70, 2, -200, 3, -550, 4, -750, 'Shop', -950, 'Mortgage value', -90, 'House cost', -100, 'Shop cost', '100 and 4 houses'], ['New York Avenue', 1, -80, 2, -220, 3, -600, 4, -800, 'Shop', -1000, 'Mortgage value', -100, 'House cost', -110, 'Shop cost', '100 and 4 houses'],
                       ['Kentucky Ave', 1, -90, 2, -250, 3, -700, 4, -875, 'Shop', -1050, 'Mortgage value', -110, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Indiana Avenue', 1, -90, 2, -250, 3, -700, 4, -875, 'Shop', -1050, 'Mortgage value', -110, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Illinois Avenue', 1, -100, 2, -300, 3, -750, 4, -925, 'Shop', -1100, 'Mortgage value', -120, 'House cost', -150, 'Shop cost', '150 and 4 houses'],
                       ['Atlantic Palace', 1, -110, 2, -330, 3, -800, 4, -975, 'Shop', -1150, 'Mortgage value', -130, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Ventor Avenue', 1, -110, 2, -330, 3, -800, 4, -975, 'Shop', -1150, 'Mortgage value', -130, 'House cost', -150, 'Shop cost', '150 and 4 houses'], ['Marvin Avenue', 1, -120, 2, -360, 3, -850, 4, -1025, 'Shop', -1200, 'Mortgage value', -140, 'House cost', -150, 'Shop cost', '150 and 4 houses'],
                       ['Pacific Ave', 1, -130, 2, -390, 3, -900, 4, -1100, 'Shop', -1275, 'Mortgage value', -150, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['NC Avenue', 1, -130, 2, -390, 3, -900, 4, -1100, 'Shop', -1275, 'Mortgage value', -150, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['Pennsylvania Avenue', 1, -150, 2, -450, 3, -1000, 4, -1200, 'Shop', -1400, 'Mortgage value', -160, 'House cost', -200, 'Shop cost', '200 and 4 houses'],
                       ['Park Avenue', 1, -175, 2, -500, 3, -1100, 4, -1300, 'Shop', -1500, 'Mortgage value', -175, 'House cost', -200, 'Shop cost', '200 and 4 houses'], ['Broad Walk', 1, -200, 2, -600, 3, -1400, 4, -1700, 'Shop', -20500, 'Mortgage value', -200, 'House cost', -200, 'Shop cost', '200 and 4 houses'],
                       ['Electric Company', 1, -(self.dice*4), 2, -(self.dice*10)],['Water Works', 1, -(self.dice*4), 2, -(self.dice*10)],
                       ['Reading Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['Pennsylvania Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['B&O Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100], ['Short Line Railroad', 1, -25, 2, -50, 3, -100, 4, -200, 'Mortgage Value', -100]]
        # board[[spot, (color, property, price), [people on this spot]]
        self.board = [[0, ('none', "GO", 200), []], [1, ('Brown', 'Mediterranean Ave', -60), []],
                      [2, ("none", 'Community chest', 0), []], [3, ('Brown', 'Baltic Avenue', -60), []],
                      [4, ('none', 'Income Tax', -200), []], [5, ('none', 'Reading Railroad', -200), []],
                      [6, ('Blue', 'Oriental Avenue', -100), []], [7, ('none', 'Chance', 0), []],
                      [8, ('Blue', 'Vermont Avenue', -100), []], [9, ('Blue', 'Connecticut Avenue', -120), []],
                      [10, ('none', "In Jail", 0), []], [11, ('Pink', 'St Charles Place', -140), []],
                      [12, ("none", 'Electric Company', 0)], [13, ('Pink', 'State Avenue', -140), []],
                      [14, ('Pink', 'Virginia Avenue', -160), []], [15, ('none', 'Pennsylvania Railroad', -200), []],
                      [16, ('Orange', 'St James Palace', -180), []], [17, ('none', 'Community Chest', 0), []],
                      [18, ('Orange', 'Tennessee Avenue', -180), []], [19, ('Orange', 'New York Avenue', -200), []],
                      [20, ('none', "Free Parking", 0), []], [21, ('Red', 'Kentucky Ave', -220), []],
                      [22, ("none", 'Chance', 0), []], [23, ('Red', 'Indiana Avenue', -220), []],
                      [14, ('Red', 'Illinois Avenue', -240), []], [25, ('none', 'B&O Railroad', -200), []],
                      [26, ('Yellow', 'Atlantic Palace', -260), []], [17, ('Yellow', 'Ventor Avenue', -260), []],
                      [28, ('none', 'Water Works', -150), []], [29, ('Yellow', 'Marvin Avenue', -280), []],
                      [30, ('none', "Go to Jail", 0), []], [31, ('Green', 'Pacific Ave', -300), []],
                      [32, ("Green", 'NC Avenue', -300), []], [33, ("none", 'Community chest', 0), []],
                      [14, ('Green', 'Pennsylvania Avenue', -320), []], [35, ('none', 'Short Line Railroad', -200), []],
                      [36, ("none", 'Chance', 0), []], [37, ('Purple', 'Park Avenue', -350), []],
                      [38, ('none', 'Luxury Tax', -100), []], [29, ('Purple', 'Broad Walk', -400), []]]
        self.cash = 20580

    def roll(self):
        die1 = random.choice([1, 2, 3, 4, 5, 6])
        die2 = random.choice([1, 2, 3, 4, 5, 6])
        self.dice = die1+die2

    def play(self):
        player1name = input("Please type in your name. Player 1: ")
        player2name = input("Please type in your name. Player 2: ")
        player3name = input("Please type in your name. Player 3: ")
        self.p1 = PlayerMonopoly(player1name, 1500, player1name[0].upper())
        self.p2 = PlayerMonopoly(player2name, 1500, player2name[0].upper())
        self.p3 = PlayerMonopoly(player3name, 1500, player3name[0].upper())
        self.continued = True

        while self.p1.pcash + self.p2.pcash + self.p3.pcash == 0 or not self.continued:
            self.cash -= 4500


