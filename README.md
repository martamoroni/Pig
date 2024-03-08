# Pig Dice Game



## About the Game
- Pig is a game played with either 1 or 2 people
- The player can either roll or hold
- If a 1 is rolled the players turn ends
- The goal is to reach 100 points

## Rules
- During a players turn they have 2 options they can roll or stand.
    - Roll: roll the dice if it is a 1 your turn ends and no points are received, else the dice is added to your round total.
    - Stand: if you stand the current round total will be added to you score and the other players turn begins.

- The first person to stand with 100 points or more wins the game.

## Installation
Make sure you have make installed.
With the terminal navigate to the location you want the game and execute this command:

```
git clone https://github.com/martamoroni/Pig.git
```

Go into the Pig directory that was just created and start create the venv:

```
make venv
```
start the venv with either 
```
. .venv/Scripts/activate
```
for windows or 
```
.venv/bin/activate
```
for Unix and Macs

install the dependencies
```
make install
```


## Play the game

the game can either be started by executing the main file in the pig directory or by executing:
```
make start
```
Once in the game you can type help to see all available commands. If you have questions about the function of any command use help followes by the command in questions for an explanation.

## Intelligence 
The game implements 3 different levels of difficulty.

The easiest difficulty functions using a random number generator where is has a 1 in 10 chance of holding instead of rolling.

The medium difficulty uses the hold at 20 strategy that is 8% worse then optimal play.

For the higest difficulty we used the optimal strategy. This strategy was obtained by extracting the 3D data from the model that can be found in this [Paper](https://cupola.gettysburg.edu/cgi/viewcontent.cgi?article=1003&context=csfac). This data was then converted into a dictionary dictionary and referenced in the program.

## Documentation
To regenerate the documentation from the code, including the UML diagrams, go to the root directory of the project and execute this command:
```
make doc
```
