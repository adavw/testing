somelist = [1, 2, 3, 4, 5, 6]

def listsort(num):
    """Test docstring for this sorting function."""
    if num > 3:
        return num

sortedlist = filter(listsort, somelist)
y = 0
listsort(y)

for x in sortedlist:
    print(x)

