total_test_case = int(input())
mylist = []
mysublist = []
for i in range(total_test_case):
    n = input()
    mysublist = n.split(" ")
    mylist.append(mysublist)

for i in range(total_test_case):
    try:
        a = int(mylist[i][0])
        b = int(mylist[i][1])
        print(a/b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)