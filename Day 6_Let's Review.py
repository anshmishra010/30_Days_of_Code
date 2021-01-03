# n=int(input())
# for i in range(n):
#     data =input().rstrip()
#     even = []
#     odd = []

#     i=0
#     while(i<len(data)):

#         even.append(data[i])
#         i+=1
#         if(i<len(data)):
#             odd.append(data[i])
#         i+=1

#     even=''.join(even)
#     odd=''.join(odd)
#     print(even,odd)

# another method

n = int(input())
for i in range(n):
    data = input()
    even = ''
    odd = ''

    for j in range(len(data)):
        if (j % 2 == 0):
            even += data[j]
        else:
            odd += data[j]
    print('{} {}'.format(even, odd))