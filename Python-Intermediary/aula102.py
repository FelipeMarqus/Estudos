def externa(x):
    def interna():
        return x + 10
    return interna


print(externa(10))