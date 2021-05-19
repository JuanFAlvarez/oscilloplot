import fileinput

X = []
Y = []

every_n = 2  # we throw away every other pixel to improve the refresh rate

i = 0
for line in fileinput.input():
    i += 1
    if i % every_n != 0: continue
    x, y = line.strip().split(",")
    X.append(x)
    Y.append(y)

print("byte x_points[NUM_POINTS] = {%s};" % ','.join(X))
print("byte y_points[NUM_POINTS] = {%s};" % ','.join(Y))
print(len(X))


#call python trimpoints.py swag.txt > swag2.txt
