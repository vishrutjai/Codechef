a = input()
for x in range(a):
    n = raw_input()
    if n == 'b' or n == 'B':
        print 'BattleShip'
    elif n == 'c' or n =='C':
        print 'Cruiser'
    elif n == 'd' or n == 'D':
        print 'Destroyer'
    else:
        print 'Frigate'







'''
Class ID	Ship Class
B or b	BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate
'''