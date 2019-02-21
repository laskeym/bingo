import random
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


class BingoCard:
    def __init__(self):
        self.bingo_mapping = {0: 'B', 1: 'I', 2: 'N', 3: 'G', 4: 'O'}
        self.bingo_card = []

        self.generate_bingo_card()

        self.bingo_card[2][2] = 'Free'

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
        for i in range(0, 5):
            print(self.bingo_mapping[i] + "\t", end='')
        print('')
        print('-'*35)

        # print(self.bingo_card)

        for row in self.bingo_card:
            for num in row:
                print(str(num) + "\t", end='')
            print('')  


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
    cards = input_number()
        
    card_list = []
    for i in range(0, cards):
        card_list.append(BingoCard())

    for bingo_card in card_list:
        bingo_card.print_bingo_card()

if __name__ == '__main__':
    main()