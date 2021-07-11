nums = [3, 4, 1, 2, 30, 50, 90]

b = list()
c = list()


def makeOddorNotlist():
    for a in range(len(nums)):
        if nums[a] % 2:
            c.append(nums[a])
        else:
            b.append(nums[a])
    print(b)
    print(c)


makeOddorNotlist()
