import fileinput
# input is .txt list of coordinates in form: x,y
# output is .txt list of code to paste on arduino IDE
X = []
Y = []

every_n = 2  # remove every other pixel to increase refresh rate
i = 0
for line in fileinput.input():
    i += 1
    if i % every_n != 0: continue
    x, y = line.strip().split(",")
    X.append(x)
    Y.append(y)
print("const unsigned long x_points[NUM_POINTS] = {%s};" % ','.join(X))
print("const unsigned long y_points[NUM_POINTS] = {%s};" % ','.join(Y))
print(len(X))

#call python trimpoints.py inputlist.txt > arduino_list.txt
