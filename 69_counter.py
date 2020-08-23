from collections import Counter
X = int(input())
shoes_sizes = input()
shoes_list = shoes_sizes.split(" ")
shoes = []
sum = 0
for i in range(len(shoes_list)):
    integer = int(shoes_list[i])
    shoes.append(integer)

counter = Counter(shoes)

N = int(input())

for i in range(0,N):
    customer = input()
    cust_list = []
    cust = customer.split(" ")
    for j in range(len(cust)):
        integer = int(cust[j])
        cust_list.append(integer)
    try:
        if counter[cust_list[0]] == 0:
            sum += 0
        else:
            val = counter[cust_list[0]] - 1
            counter[cust_list[0]] = val 
            sum += cust_list[1]
    except:
        pass
print(sum)

