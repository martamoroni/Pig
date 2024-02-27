# Pig Dice Game

## About the Game
- Pig is a game played with either 1 or 2 people
- The player can either roll or hold
- If a 1 is rolled the players turn ends
- The goal is to reach 100 points

## Rules
- During a players turn they have 2 options they can roll or stand.
    - Roll: roll the dice if it is a 1 your turn ends and no points are recived, else the dice is added to your round total.
    - Stand: if you stand the current round total will be added to you score and the other players turn begins.

- The first person to stand with 100 points or more wins the game.

## Installation
Make sure you have make installed.
With the terminal navigate to the location you want the game and execute this command:

```
git clone https://github.com/martamoroni/Pig.git
```

Go into the Pig directory that was just created and start creat the venv:

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

install the dependencices
```
make install
```


## Play the game

the game can either be started by executing the main file in the pig directory or by executing:
```
make start
```
Once in the game you can type help to see all available commands. If you have questions about the function of any command use help followes by the command in questions for an explenation.
