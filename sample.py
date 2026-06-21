# S = "hello"
# rev = ""
# for ch in S:
#     rev = ch +rev
# print(rev)

# i = 1
# while(i<=100):
#     print(i)
#     i+=1


# i = 100
# while(i>=1):
#     print(i)
#     i-=1

# l1 =[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for i in l1:
#     print(i)

# i = 1
# while(i<=10):
#     print(i*i)
#     i+=1

# i = 1
# for i in range(1, 11):
#     print(i*i)

i = 0
tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
e = (input("please enter a number:"))
while(i<len(tup1)):
     if(e==int(tup1[i])):
            print("number is present in the tuple")
            break
i+=1
