import A_star

def main():

    grid = [
        [9, 2, 3, 0, 4, 6, 0, 0, 1, 9, 7, 6, 5, 0, 3, 0, 2, 1, 8, 9],
        [1, 0, 0, 0, 5, 0, 6, 2, 3, 1, 0, 9, 0, 8, 4, 5, 6, 7, 0, 1],
        [2, 1, 9, 8, 0, 3, 0, 4, 0, 2, 5, 0, 0, 1, 3, 7, 0, 6, 9, 2],
        [0, 0, 1, 0, 2, 0, 7, 5, 0, 3, 0, 4, 8, 2, 0, 1, 4, 0, 2, 3],
        [6, 7, 0, 4, 0, 1, 0, 6, 3, 7, 0, 0, 2, 3, 5, 8, 6, 1, 0, 9],
        [8, 3, 4, 6, 1, 2, 9, 0, 7, 5, 3, 0, 0, 9, 0, 2, 7, 3, 5, 0],
        [9, 0, 0, 2, 0, 5, 1, 0, 0, 2, 6, 4, 0, 0, 3, 4, 1, 0, 6, 2],
        [1, 6, 5, 7, 0, 4, 0, 9, 1, 3, 0, 8, 2, 5, 6, 0, 3, 0, 1, 4],
        [0, 4, 0, 3, 2, 1, 8, 7, 0, 0, 0, 5, 3, 4, 2, 9, 0, 1, 7, 0],
        [3, 7, 6, 8, 0, 9, 5, 1, 2, 4, 0, 6, 9, 0, 8, 3, 2, 5, 4, 6],
        [4, 0, 0, 1, 3, 0, 2, 7, 0, 0, 0, 1, 0, 5, 4, 0, 0, 6, 0, 9],
        [5, 8, 9, 0, 2, 4, 0, 0, 0, 5, 7, 0, 0, 2, 6, 7, 0, 1, 9, 8],
        [0, 0, 2, 5, 1, 0, 0, 8, 6, 4, 3, 0, 2, 0, 7, 5, 1, 0, 3, 6],
        [3, 1, 0, 6, 0, 7, 9, 0, 2, 0, 8, 5, 0, 4, 3, 9, 0, 2, 6, 0],
        [9, 4, 6, 3, 2, 1, 0, 0, 5, 6, 7, 0, 1, 3, 0, 0, 8, 4, 0, 2],
        [0, 0, 8, 9, 0, 0, 2, 1, 0, 3, 4, 0, 6, 7, 5, 0, 2, 0, 7, 9],
        [6, 9, 0, 0, 4, 5, 3, 8, 0, 1, 0, 0, 7, 0, 6, 4, 3, 2, 1, 0],
        [2, 0, 1, 3, 0, 6, 0, 0, 2, 0, 5, 0, 3, 1, 4, 6, 0, 0, 9, 8],
        [1, 3, 5, 7, 8, 0, 0, 9, 6, 2, 1, 3, 0, 8, 2, 0, 0, 7, 6, 0],
        [7, 0, 2, 4, 0, 3, 1, 0, 8, 9, 0, 2, 5, 6, 0, 7, 1, 0, 0, 4]
    ]

    src = [0,0]

    dest = [19,3]

    A_star.a_star_search(grid,src,dest)

if __name__ == "__main__":
    main()
