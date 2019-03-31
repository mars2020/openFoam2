import math

## define r 
r = 1
verts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
v2 = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
theta = [1, 3, 5, 7, 9, 11, 13, 15]
theta = [x*.393 for x in theta] 
#for i in verts:
#    for j in theta
#    print('arc {} {} ({} {} 0)'.format(verts[i], verts[i+1], r*math.cos(.393*), r*math.sin()))


print('arc 0 1 ({} {} 0)'.format(r*math.cos(.393*1), r*math.sin(.393*1)))
print('arc 1 2 ({} {} 0)'.format(r*math.cos(.393*3), r*math.sin(.393*3)))
print('arc 2 3 ({} {} 0)'.format(r*math.cos(.393*5), r*math.sin(.393*5)))
print('arc 3 4 ({} {} 0)'.format(r*math.cos(.393*7), r*math.sin(.393*7)))
print('arc 4 5 ({} {} 0)'.format(r*math.cos(.393*9), r*math.sin(.393*9)))
print('arc 5 6 ({} {} 0)'.format(r*math.cos(.393*11), r*math.sin(.393*11)))
print('arc 6 7 ({} {} 0)'.format(r*math.cos(.393*13), r*math.sin(.393*13)))
print('arc 7 0 ({} {} 0)'.format(r*math.cos(.393*15), r*math.sin(.393*15)))

print('arc 8 9 ({} {} 0)'.format(r*math.cos(.393*1), r*math.sin(.393*1)))
print('arc 9 10 ({} {} 0)'.format(r*math.cos(.393*3), r*math.sin(.393*3)))
print('arc 10 11 ({} {} 0)'.format(r*math.cos(.393*5), r*math.sin(.393*5)))
print('arc 11 12 ({} {} 0)'.format(r*math.cos(.393*7), r*math.sin(.393*7)))
print('arc 12 13 ({} {} 0)'.format(r*math.cos(.393*9), r*math.sin(.393*9)))
print('arc 13 14 ({} {} 0)'.format(r*math.cos(.393*11), r*math.sin(.393*11)))
print('arc 14 15 ({} {} 0)'.format(r*math.cos(.393*13), r*math.sin(.393*13)))
print('arc 15 8 ({} {} 0)'.format(r*math.cos(.393*15), r*math.sin(.393*15)))

print('arc 32 33 ({} {} 0.1)'.format(r*math.cos(.393*1), r*math.sin(.393*1)))
print('arc 33 34 ({} {} 0.1)'.format(r*math.cos(.393*3), r*math.sin(.393*3)))
print('arc 34 35 ({} {} 0.1)'.format(r*math.cos(.393*5), r*math.sin(.393*5)))
print('arc 35 36 ({} {} 0.1)'.format(r*math.cos(.393*7), r*math.sin(.393*7)))
print('arc 36 37 ({} {} 0.1)'.format(r*math.cos(.393*9), r*math.sin(.393*9)))
print('arc 37 38 ({} {} 0.1)'.format(r*math.cos(.393*11), r*math.sin(.393*11)))
print('arc 38 39 ({} {} 0.1)'.format(r*math.cos(.393*13), r*math.sin(.393*13)))
print('arc 39 32 ({} {} 0.1)'.format(r*math.cos(.393*15), r*math.sin(.393*15)))

print('arc 40 41 ({} {} 0.1)'.format(r*math.cos(.393*1), r*math.sin(.393*1)))
print('arc 41 42 ({} {} 0.1)'.format(r*math.cos(.393*3), r*math.sin(.393*3)))
print('arc 42 43 ({} {} 0.1)'.format(r*math.cos(.393*5), r*math.sin(.393*5)))
print('arc 43 44 ({} {} 0.1)'.format(r*math.cos(.393*7), r*math.sin(.393*7)))
print('arc 44 45 ({} {} 0.1)'.format(r*math.cos(.393*9), r*math.sin(.393*9)))
print('arc 45 46 ({} {} 0.1)'.format(r*math.cos(.393*11), r*math.sin(.393*11)))
print('arc 46 47 ({} {} 0.1)'.format(r*math.cos(.393*13), r*math.sin(.393*13)))
print('arc 47 40 ({} {} 0.1)'.format(r*math.cos(.393*15), r*math.sin(.393*15)))


