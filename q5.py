for i in range(0,10**10,20):
    divisible = True
    for j in range(1,21):
        if i%j != 0:
            divisible = False
            break
    if divisible == True:
        print(i)

# for n in range (1,9999999999):
#     if n % 1 ==0:
#         if n % 2 ==0:
#             if n % 3 ==0:
#                 if n % 4 ==0:
#                     if n % 5 ==0:
#                         if n % 6 ==0:
#                             if n % 7 ==0:
#                                 if n % 8 ==0:
#                                     if n % 9 ==0:
#                                         if n % 10 ==0:
#                                             if n % 11 ==0:
#                                                 if n % 12 ==0:
#                                                     if n % 13 ==0:
#                                                         if n % 14 ==0:
#                                                             if n % 15 ==0:
#                                                                 if n % 16 ==0:
#                                                                     if n % 17 ==0:
#                                                                         if n % 18 ==0:
#                                                                             if n % 19 ==0:
#                                                                                 if n % 20 ==0:
#                                                                                     print(n)