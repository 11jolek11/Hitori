# Hitori
Hitori (Japanese: "Alone" or "one person"; ひとりにしてくれ Hitori ni shite kure; literally "leave me alone") is a type of logic puzzle
Hitori is NP complete.
### Rules
Hitori is played with a grid of squares or cells, with each cell initially containing a number. The game is played by eliminating squares/numbers and this is done by blacking them out. The objective is to transform the grid to a state wherein all three following rules are true:
- no row or column can have more than one occurrence of any given number
- black cells cannot be horizontally or vertically adjacent, although they can be diagonal to one another.
- the remaining numbered cells must be all connected to each other, horizontally or vertically.

### Files
hitori.mod - CPLEX solution
task.dat - data for solver
converter.py - converts from python puzzle instance representation to solver representation and saves in task.dat
meta.py - implementation of heuristic algorithm
problems.py - example problems with solutions
hitori_cp.py - test and validation of hitori.mod results
