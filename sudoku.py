import numpy as np
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# |%%--%%| <b3TgJUhR8w|ANKd3ex4To>

print(grid)

# |%%--%%| <ANKd3ex4To|BAO69wVIBf>



# |%%--%%| <BAO69wVIBf|mVtFSyeKNZ>

print(np.matrix(grid))

# |%%--%%| <mVtFSyeKNZ|C5CaEumdM6>
"""°°°
## Funzione analizza possibilità inserimento numero nella posizione aperta
°°°"""
# |%%--%%| <C5CaEumdM6|xGNv33EtL9>
"""°°°
X = colonna Y = riga N = numero da verificare
°°°"""
# |%%--%%| <xGNv33EtL9|o5U2s5NzDt>

def possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

# |%%--%%| <o5U2s5NzDt|INJQnVJSU2>
"""°°°
Verifichiamo se possiamo inserire N nella posizione centrale (indice parte da ZERO)
°°°"""
# |%%--%%| <INJQnVJSU2|6aa5PPPgy7>

possible(4, 4, 3)

# |%%--%%| <6aa5PPPgy7|N5cXbJjMr9>

possible(4, 4, 6)

# |%%--%%| <N5cXbJjMr9|hhPqQsmGzZ>

possible(4, 4, 5)

# |%%--%%| <hhPqQsmGzZ|edFNEh4Lkd>

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

# |%%--%%| <edFNEh4Lkd|OPetehAD9T>

solve()

# |%%--%%| <OPetehAD9T|AHptEq7zjk>


