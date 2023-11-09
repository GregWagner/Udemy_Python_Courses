import random
import tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    extension = 'png' if tkinter.TkVersion >= 8.6 else 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = f"cards/{card}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # and add it back to the end of the deck
    deck.append(next_card);
    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card

def shuffle_deck():
    random.shuffle(deck)


def score_hand(hand):
    """
    Calculate the total score of all cards in the hand
    Only on ace can have the value 11, and this will be rediced to 1 if the 
    hand would have busted
    """
    score = 0
    ace = False
    for card in hand:
        card_value = card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            ace = False
            score -= 10
    return score


def deal_to_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    if dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw!!!")


def deal_to_player():
    player_hand.append(deal_card(player_card_frame))
    score = score_hand(player_hand)
    player_score_label.set(score)
    if score > 21:
        result_text.set("Dealer Wins!")


def new_game():
    global dealer_card_frame
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    global player_card_frame
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    player_hand.clear()
    dealer_hand.clear()

    deal_initial_hands()


def deal_initial_hands():
    deal_to_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_to_player()


def play_game():
    deal_initial_hands()

    # pass conntrol to tk
    main_window.mainloop()



main_window = tkinter.Tk()
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.config(background="green")

# setup the screen and frames for the dealer and player
result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame=tkinter.Frame(main_window, relief="sunken", borderwidth=1,
                         background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green",
              fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green",
              fg="white").grid(row=1, column=0)
# embedded frame holds the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green",
              fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green",
              fg="white").grid(row=3, column=0)
# embedded frame holds the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer",
                               command=deal_to_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player",
                               command=deal_to_player)
player_button.grid(row=0, column=1)

new_button = tkinter.Button(button_frame, text="New Game",
                               command=new_game)
new_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle",
                                 command=shuffle_deck)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)

# create a new desk of cards and shuffle them
deck = cards[:]
shuffle_deck()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

#new_game()


if __name__ == "__main__":
    play_game()

