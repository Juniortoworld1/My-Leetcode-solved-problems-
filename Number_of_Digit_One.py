def count1(n):
    count = 0 
    while 1<n:
        count+=str(n).count('1')
        n-=1
    
    print(count)

n = int(input("enter the number : "))
count1(n)
