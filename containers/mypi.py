# simple implementation of the Leibniz formula to compute pi
pi = 0
accuracy = 1000000
for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))
    print(pi)