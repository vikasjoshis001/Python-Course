n = int(input())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)
# print("Block 1")
# # result = average(n,arr)
# # print(arr)
# # k = 1
# # print(arr.pop(k))
# # print(arr)
# # print(len(arr))

# # def average(N,array):
    
# height = {0,0}
# l = len(arr)
# value = []
# print("len = ",l)
# print("Block 2")
# for i in range(len(arr)):
#     print("Block 3")
#     m = len(arr)
#     # print(i)
#     Z = i+1
#     # print(Z)
#     if (Z == len(arr)):
#         print("Block 4")
#         break
#     else:
#         while(Z != m):
#             if arr[i] == arr[Z]:
#                 print("Block 5")
#                 # print(arr[Z])
#                 value.append(arr[i])
#                 arr.pop(Z)
#                 Z+=1
#                 print("#################################################################",value[i])
#                 print("......................................................................",Z)
#                 # print("kkk")
#             else:
#                 print("Block 6")
#                 # print(arr[Z])
#                 Z+=1
#                 print(".........................................................................",Z)
#     Z = 0
#     print("Block 7")
#     # print(arr[i])
#     # print(arr[Z])
# print(value)

arr = list(dict.fromkeys(arr))
print(arr)
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
avg = sum/len(arr)
print(avg)


