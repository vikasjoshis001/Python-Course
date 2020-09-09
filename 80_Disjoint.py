# -----------------------------------METHOD 1----------------------------------------

# import time
# start = time.time()
# str = input()
# strN = input()
# strA = input()
# strB = input()
# score = 0

# Nlist = strN.split(" ")
# newNlist = list(map(int,Nlist))

# Alist = strA.split(" ")
# newAlist = list(map(int,Alist))

# Blist = strB.split(" ")
# newBlist = list(map(int,Blist))

# for i in range(len(newNlist)):
#     for j in range(len(newAlist)):
#         if (int(newNlist[i]) == int(newAlist[j])):
#             print("A = ",newAlist[j])
#             score += 1
#     for k in range(len(newBlist)):
#         if (int(newNlist[i]) == int(newBlist[k])):
#             print("B = ",newBlist[k])
#             score -= 1

# print(score)
# end = time.time()
# print("Runtime of the program is ",end - start)


# --------------------------------------METHOD 2---------------------------------------------

# str = input()
# strN = input()
# strA = input()
# strB = input()

# setN = set()
# setA = set()
# setB = set()
# setC = set()
# setD = set()

# score = 0

# Nlist = strN.split(" ")
# newNlist = list(map(int,Nlist))

# Alist = strA.split(" ")
# newAlist = list(map(int,Alist))

# Blist = strB.split(" ")
# newBlist = list(map(int,Blist))

# for i in range(len(Nlist)):
#     setN.add(Nlist[i])

# for i in range(len(Alist)):
#     setA.add(Alist[i])

# for i in range(len(Blist)):
#     setB.add(Blist[i])

# setC = setN.intersection(setA)
# score += len(setC)
# # print("score 1 =",score)


# setD = setN.intersection(setB)
# # val = len(setD)
# # print("Value ",val)
# score = score-len(setD)
# # print("score 2 =",score)


# # print(setN)
# # print(setA)
# # print(setB)
# # print(setC)
# # print(setD)

# print(score)

# ----------------------------METHOD 3---------------------------------------------

# strS = input()
# strN = input()
# strA = input()
# strB = input()

# listN = []
# listA = []
# listB = []
# listC = []
# listD = []

# score = 0

# listN = strN.split(" ")
# listA = strA.split(" ")
# listB = strB.split(" ")

# listN = list(map(int,listN))
# listA = list(map(int,listA))
# listB = list(map(int,listB))

# listC = [value for value in listN if value in listA]
# listD = [value for value in listN if value in listB]

# print(listC)
# print(listD)
# print(score)

# -------------------------------------------METHOD 4------------------------------------------

# import time
# start = time.time()

# strS = input()
# strN = input()
# strA = input()
# strB = input()

# score = 0

# listS = strS.split(" ")
# listN = strN.split(" ")
# listA = strA.split(" ")
# listB = strB.split(" ")

# n = int(listS[0])
# m = int(listS[1])
# listN = list(map(int,listN))
# listA = list(map(int,listA))
# listB = list(map(int,listB))

# listN.sort()
# listA.sort()
# listB.sort()

# for i in range(len(listN)):
#     count = 0
#     l = 0;
#     u = m-1
#     while(u>=1):
#         mid = int((l+u)/2)
#         if (listN[i] == listA[mid]):
#             print("A = ",listA[mid])
#             score += 1
#             break;
#         elif (listN[i]<listA[mid]):
#             count+=1
#             if (count == m):
#                 break;
#             u = mid-1
#         else:
#             count+=1
#             if (count == m):
#                 break;
#             l = mid + 1

# for i in range(len(listN)):
#     count = 0  
#     l = 0
#     u = m - 1         
#     while(u>=1):
#         mid = int((l+u)/2)
#         if (listN[i] == listB[mid]):
#             print("B = ",listB[mid])
#             score -= 1
#             break;
#         elif (listN[i]<listB[mid]):
#             count+=1
#             if (count == m):
#                 break;
#             u = mid-1
#         else:
#             count+=1
#             if (count == m):
#                 break;
#             l = mid + 1

# print(score)
# print("score = ",score)
# end = time.time()
# print("Runtime of the program is ",end - start)









