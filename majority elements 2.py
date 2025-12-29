def majorityElement(nums):
    c1=0
    c2=0
    num1=num2=0
    for num in nums:
        if num ==num1:
            c1+=c1 
        elif num==num2:
                c2+=c1
        elif c1==0:
             num1=num2
             c2=c1
         else:
             c1-=c1
             c2-=c1
         print(num1,num2)
nums=list(map(int,input().split()))
majorityElement(nums)
                