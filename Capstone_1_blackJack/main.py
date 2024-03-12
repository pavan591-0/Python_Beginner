import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealCards():
  """returns a random card from the deck"""
  return random.choice(cards)


def check_status(usrscore, comscore):
  """checks the status of the game"""
  if usrscore == comscore:
    if usrscore <= 21:
      print("It's a Draw😏")
    else:
      print("You lose!😵")
  elif usrscore == 21:
    print("You win!😀")
  elif comscore == 21:
    print("You lose!😵")
  elif usrscore > 21:
    print("You lose!😵")
  elif comscore > 21:
    print("You win!😀")
  else:
    if usrscore > comscore:
      print("You win!😀")
    else:
      print("You lose!😵")


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)



def black_jack(usrscore, compscore):
  if usrscore == 0:
    print("You won, Its a black jack 😁")
  elif compscore == 0:
    print("You lose, Its a black jack 😵")
  elif usrscore > 21:
    print("You lose, you went over 21 😵")
  else:
    return False

def playGame():
  print(logo)
  dealer_cards = []
  user_cards = []
  for i in range(0, 2):
    dealer_cards.append(dealCards())
    user_cards.append(dealCards())

  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)

  print(f"your cards: {user_cards} and the current score is {user_score}")
  print(f"computer's first card: {dealer_cards[0]}")

  is_blackJack = black_jack(user_score, dealer_score)

  if not is_blackJack:
    card_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if (card_choice == 'y'):
      user_cards.append(dealCards())
      user_score = calculate_score(user_cards)

    if (dealer_score < 17):
      dealer_cards.append(dealCards())
      dealer_score = calculate_score(dealer_cards)

    print(f"Your Final hand is {user_cards}, final score is {user_score}")
    print(
        f"Computer's final hand is {dealer_cards}, final score is {dealer_score}"
    )
    check_status(user_score, dealer_score)

choice = input("Do you want to play black jack? type 'y' or 'n': ")

while choice == 'y':
  clear()
  playGame()
  choice = input("Do you want to play black jack? type 'y' or 'n': ")

print("Thanks for playing Black Jack")
