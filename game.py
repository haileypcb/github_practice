import random

# Define constants for colors and values
COLORS = ['Red', 'Green', 'Blue', 'Yellow']
VALUES = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two']
SPECIAL_CARDS = ['Wild', 'Wild Draw Four']

# Create the deck of cards
def create_deck():
    deck = []
    for color in COLORS:
        for value in VALUES:
            deck.append((color, value))
            if value != '0':  # Each card except '0' has a pair
                deck.append((color, value))
    for special in SPECIAL_CARDS:
        deck.append((None, special))  # Wild cards are colorless
        deck.append((None, special))
        deck.append((None, special))
        deck.append((None, special))
    return deck

# Draw a card from the deck
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Initialize the game
def initialize_game():
    deck = create_deck()
    random.shuffle(deck)
    player_hand = [draw_card(deck) for _ in range(7)]
    computer_hand = [draw_card(deck) for _ in range(7)]
    discard_pile = [draw_card(deck)]
    return deck, player_hand, computer_hand, discard_pile

# Print the current state of the hands
def print_hands(player_hand, computer_hand):
    print("\nYour hand:")
    for index, card in enumerate(player_hand):
        print(f"{index + 1}: {card}")
    print("\nComputer's hand: [Hidden]")

# Play the game
def play_game():
    deck, player_hand, computer_hand, discard_pile = initialize_game()
    game_over = False
    current_color = discard_pile[-1][0]
    current_value = discard_pile[-1][1]
    
    while not game_over:
        print(f"\nCurrent discard pile: {discard_pile[-1]}")
        print(f"Current color: {current_color}, Current value: {current_value}")
        print("Your turn!")
        
        print_hands(player_hand, computer_hand)
        
        try:
            choice = int(input("Enter the number of the card you want to play (or 0 to draw a card): "))
            if choice == 0:
                new_card = draw_card(deck)
                print(f"You drew: {new_card}")
                player_hand.append(new_card)
            else:
                chosen_card = player_hand[choice - 1]
                if chosen_card[0] == current_color or chosen_card[1] == current_value or chosen_card[0] is None:
                    discard_pile.append(chosen_card)
                    player_hand.pop(choice - 1)
                    current_color = chosen_card[0] if chosen_card[0] is not None else current_color
                    current_value = chosen_card[1]
                    if not player_hand:
                        print("Congratulations! You won!")
                        game_over = True
                else:
                    print("Invalid move! Try again.")
        except (IndexError, ValueError):
            print("Invalid input! Try again.")
        
        # Computer's turn (very basic AI)
        if not game_over:
            valid_moves = [card for card in computer_hand if card[0] == current_color or card[1] == current_value or card[0] is None]
            if valid_moves:
                chosen_card = random.choice(valid_moves)
                discard_pile.append(chosen_card)
                computer_hand.remove(chosen_card)
                current_color = chosen_card[0] if chosen_card[0] is not None else current_color
                current_value = chosen_card[1]
                print(f"Computer played: {chosen_card}")
                if not computer_hand:
                    print("Computer won! Better luck next time.")
                    game_over = True
            else:
                new_card = draw_card(deck)
                print(f"Computer drew: {new_card}")
                computer_hand.append(new_card)
            
        # Check if the deck is empty
        if not deck:
            print("The deck is empty. Game ends in a draw!")
            game_over = True

if __name__ == "__main__":
    play_game()