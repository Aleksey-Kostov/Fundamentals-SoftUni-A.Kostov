deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffles in range(count_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_parts = deck_of_cards[0:middle_of_the_deck]
    right_parts = deck_of_cards[middle_of_the_deck:]
    for card_index in range(len(left_parts)):
        final_deck.append(left_parts[card_index])
        final_deck.append(right_parts[card_index])
    deck_of_cards = final_deck
final_deck = deck_of_cards
print(final_deck)
