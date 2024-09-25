fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(4300)]
print(fibonacci)
