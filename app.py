import random
import time
from pprint import pprint


def bingo_numbers_list():
  bingo_numbers = []
  start = 1
  end = 16

  while end <= 76:
      bingo_numbers.append(list(range(start, end)))
      start = end
      end = end + 15

  return bingo_numbers


w_struct = [
  [(0, 0), (0,1), (0, 2), (0, 3), (0, 4)],
  [(0, 0), (1,1), (2, 2), (3, 3), (4, 4)]
]

class Game:
    def __init__(self):
        self.game_over = False
        self.bingo_numbers = list(range(1, 76))
        self.called_numbers = set()
        self.winning_structure = []
        self.card_list = []

        self.winning_structure = [
          [(0,0), (0,1), (0,2), (0,3), (0,4)],
          [(1,0), (1,1), (1,2), (1,3), (1,4)],
          [(2,0), (2,1), (2,2), (2,3), (2,4)],
          [(3,0), (3,1), (3,2), (3,3), (3,4)],
          [(4,0), (4,1), (4,2), (4,3), (4,4)],
          [(0,0), (1,1), (2,2), (3,3), (4,4)],
          [(0,0), (1, 0), (2, 0), (3, 0), (4, 0)],
          [(1,0), (1, 1), (1, 2), (1, 3), (1, 4)],
          [(2,0), (2, 1), (2, 2), (2, 3), (2, 4)],
          [(3,0), (3, 1), (3, 2), (3, 3), (3, 4)],
          [(4,0), (4, 1), (4, 2), (4, 3), (4, 4)],
        ]

        random.shuffle(self.bingo_numbers)

    def get_bingo_card_list(self):
        cards = input_number()
        for i in range(0, cards):
            self.card_list.append(BingoCard())

    def update_boards(self, number_called):
        for card in self.card_list:
            card.check_if_num_called(number_called)
            # print(card.called_numbers_structure)
            self.check_for_bingo(card)

    def check_for_bingo(self, card):
        for win in self.winning_structure:
            hit_set = set(card.called_numbers_structure)
            winning_set = set(win)

            if len(winning_set.difference(hit_set)) == 0:
                self.game_over = True
                print('*'*75)
                print('BINGO!')
                print(card.print_bingo_card())
                print('*'*75)

    def play_turn(self):
        # Choose a random number, remove from list and add to called numbers set
        num = random.choice(self.bingo_numbers)
        self.bingo_numbers.remove(num)
        self.called_numbers.add(num)

        # Display last number called with latest update to boards
        print('Last Number Called:\t', str(num))
        self.update_boards(num)

    def play(self):
        self.get_bingo_card_list()

        while not self.game_over and self.bingo_numbers:
            self.play_turn()
            time.sleep(1)

        print('GAME OVER')
        exit(1)

class BingoCard:
    def __init__(self):
        self.bingo_mapping = {0: 'B', 1: 'I', 2: 'N', 3: 'G', 4: 'O'}
        self.bingo_card = []
        self.called_numbers_structure = [(0, 2)]

        self.generate_bingo_card()

        self.bingo_card[2][2] = 'Free' # Free will always be marked as a hit

    def generate_bingo_card(self):
        bingo_numbers = bingo_numbers_list()
        
        for i in range(0, 5):
            bingo_row = []
            for num_list in bingo_numbers:
                if num_list:
                  num = random.choice(num_list)
                  num_list.remove(num)
                  bingo_row.append(num)
            self.bingo_card.append(bingo_row)

    def print_bingo_card(self):
        print('-'*35)
        for i in range(0, 4):
            print(self.bingo_mapping[i] + "\t", end='')
        print('')
        print('-'*35)

        for row in self.bingo_card:
            for num in row:
                print(str(num) + "\t", end='')
            print('')  

    def check_if_num_called(self, num):
        for i, row in enumerate(self.bingo_card):
            for j, col in enumerate(row):
              if col == num:
                  self.called_numbers_structure.append((i, j))


def input_number():
    while True:
        try:
          num_card = int(input('How many Bingo Cards would you like to generate: '))
        except ValueError:
            print('Please enter a valid quantity!')
            continue
        else:
            return num_card
            break

def main():
    new_game = Game()
    new_game.play()
    # cards = input_number()
        
    # card_list = []
    # for i in range(0, cards):
    #     card_list.append(BingoCard())

    # for bingo_card in card_list:
    #     bingo_card.print_bingo_card()

if __name__ == '__main__':
    main()