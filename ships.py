#!/usr/bin/python3

ships = [ (0,9), (0,8), (0,7), (8,8),(9,8)  ]
total_ship_size = len(ships)
max_ship_size = 3
ships_hit = 0
cost = 0

def Check(x,y):
    global cost

    cost += 1
    if (x,y) in ships:
        return True
    else:
        return False

def Play(sizex, sizey):
    global ships_hit
    fields_checked = []

    for fy in range(sizey-1,-1, -1):
        for fx in range(sizex):
            # already tried
            if(fx,fy) in fields_checked:
                continue

            print(f"Shooting at coordinates: {fx},{fy}... ", end="")
            if Check(fx, fy):
                ships_hit += 1
                print("Hit!")
                if ships_hit == total_ship_size:
                    return
                (sx,sy) = (fx,fy)
                current_hits = 1
                ship_sunk = False
                while not ship_sunk and fx<sizex and fy<sizey:
                    # go right
                    while Check(fx,fy):
                        print(f"Hit right {fx},{fy}")
                        fields_checked.append((fx,fy))
                        fx += 1
                        current_hits += 1
                        if current_hits == max_ship_size:
                            ship_sunk = True
                            break
                    # go down
                    (fx,fy) = (sx,sy-1)
                    while Check(fx, fy):
                        print(f"Hit down {fx},{fy}")
                        fields_checked.append((fx,fy))
                        fy += 1
                        current_hits += 1
                        if current_hits == max_ship_size:
                            ship_sunk = True
                            break

                (fx,fy) = (sx,sy)

            else:
                print()

def Showboard(sizex, sizey, shot=(-1,-1)):
    global ships

    for fy in range(sizey-1,-1, -1):
        for fx in range(sizex):
            if (fx, fy) == shot:
                print("s", end=" ")
                continue
            if (fx,fy) in ships:
                print("X", end=" ")
            else:
                print("o", end=" ")
        print()

if __name__ == "__main__":
    #size = int(input("Enter board size: "))
    size = 10
    Showboard(size, size)
    Play(size, size)
    print(f"Total cost of shooting: {cost}")
