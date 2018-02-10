## connect_four_problem

# Problem Statement -
To implement the connect four game for two players

# Description of the game - 
Given a 5X5 grid which stands vertically and is initially empty. Each player drops a ball of their colour to a column in their turn, which sinks to the bottom. The first player to get 4 consecutive (horizontal or vertical or diagonal) slots wins.

Intrestingly, this board contains some blocked cells (manufacturing defects), where it is not possible to the coin dropped in the column to reach down (by gravity) as it is blocked by the cell in between.

# Requirements -
Create a two player version (Players can be human or computer) of the connect four game where the players take turns to add the balls to the grid from one of the columns.

For computer player, you can simply use the strategy of randomly picking any available column.

# Input - 

**start_game(game_type, blocked_cells, player_inputs)**

```
start_game('HUMAN-HUMAN', [(4,1), (5,2), (4,2), (4,4), (5,5)], [('A',1), ('B', 5), ('A', 4), ('B', 3), ('A', 2), ('B', 3), ('A', 3)])
```

```
start_game('HUMAN-COMPUTER', [(4,1), (5,2), (4,2), (4,4), (5,5)], [('A',1), ('A', 4), ('A', 2), ('A', 3)])
```

Eg:
```
start_game('HUMAN-HUMAN', [(2,2), (3,4)], [('A', 5), ('B',4), ('A', 5), ('B', 1), ('A', 5), ('B', 1), ('A', 5)])
```
```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['O'], ['O'], ['O'], ['O']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['O'], ['X'], ['O'], ['X'], ['A']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
```


```
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['O']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
```


```
Cells part of winning line - [(2, 5), (3, 5), (4, 5), (5, 5)]
FinalGameResult: A wins
[['O'], ['O'], ['O'], ['O'], ['O']]
[['O'], ['X'], ['O'], ['B'], ['A']]
[['O'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
[['B'], ['X'], ['O'], ['X'], ['A']]
```
