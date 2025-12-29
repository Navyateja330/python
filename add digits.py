def kk(nums):
    s = ""
    for num in nums:
        s += str(num)   

    i = int(s) + 1      
    z = str(i)

    k = []
    for ch in z:
        k.append(int(ch))

    print(k)

nums = [9, 9, 9]
kk(nums)
