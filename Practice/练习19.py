x = [1,2,5,3,0]
def min(x):
        least = x[0]
        for each in x:
                if each < least:
                        least = each
        return least
minimal = min(x)
print(minimal)
