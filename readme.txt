"number-guessing-game-two-player" is created in django and Rest framework.
There are two player in this game, Player and Game Master. Player will guess a number and then Game master has to guess the same number within the range.

player: We have two Python servers that have nothing better to do than play number-guessing with each other. The first server serves as the "player" and the second as the "game master". Their common language is HTTP requests. The numbers are between 1 and 1000, but are configurable.
The Player is a standalone python server that tries to find the number of gamemaster as fast as Game Master enters the number, then matches it with the player's number and tells whether the number is matched in total three attempts (configurable).

gamemaster: We have a game master server, that is capable of playing multiple game sessions at once. The game master is picking a random number inside the range so that player can match the number with the same.
