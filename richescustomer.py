
def maxwealth(accounts):
    maxlist = []
    for i in accounts:
        maxlist.append(sum(i))
        print(maxlist)
    return max(maxlist)


lists = [[1,5],[7,3],[3,5]]
print(maxwealth(lists))