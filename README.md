# David's Blackjack
#### Video Demo: https://youtu.be/OFFYoZepQgc
#### Description:
It’s a blackjack game with an interactive user interface.
I created many functions that are used in all the blckjack function.
carta_aleatoria() takes a deck and return a random card form that deck, it also deletes that card from the deck
num_carta() takes a card and returns its number
bj_sum_cartas() takes a list of cards and return the points that those cards have according to the blackjack rules
bj_hay_blackjack() checks if one player has blackjack and returns true if so
bj_poder_doblar() checks if the player can double the bet
bj_poder_rendirse() check if the player can surrender from this match.
bj_ganador() takes the cards of both players, compares them and returns -1 if the crupier wins, 0 if it's a draw, +1 if the player won and 3/2 if the player won with a blackjack
blackjack() It´s the game itself, it does nd handles everything about the game
imprimir() Takes the variables and prints them in an ordered way to create an user interface and an interactive style.
It creates a new deck every game, chooses random cards, get the points for each player and more. The game is designed to have one player against the computer. The player will be able to make decisions based on the cards they have. The default bet is 10 tokens and you will gain or lose tokens depending on the result of the game. If you get a blackjack, you will see the blackjack special message on the screen. The computer will not be able decide. because even in the real world blackjack, the croupier cannot make decisions, they have to do what the game says, so the computer’s decisions are predictable. The computer will always draw cards until they have 17 point or more. That’s a fair amount of points to always make a good decision so it is definitely not easy to win. As all the cards are random, the player will have a fair chance of winning and there are no trick under the table.
The game first starts creating variables that will be used during the whole match.
After that, the new deck is created, notice that the deck contist on a list of strings, it combines the symbols and the numbers of the cards to create a mixed list of both and that's the deck
Then it takes two random cards for the player. This is the basic behaviour of the blackjack game. You start with just two cards.
Then it checks if the player has luckily gotten a blackjack and if so, it handles that event.
If the player didn't get a blackjack, as 99% of the time, it follows the normal path of the game by showing the player their cards, adding the options that the player has available like double or surrender if the player is able to do so.
After that, the game goes to a loop. In this loop, the player will be asked to input an int depending on what action he wants to perfom.
If the wants to stop drawing, the game will show that and will pass to the next part of the game
If the player wants to draw a card, the game will draw a card for the plawer and will reset the options that the player has availible. Then it will check if the player has passed the 21 points, because if that is the case, then the player's turn will be ended and it will follow the rest of the game