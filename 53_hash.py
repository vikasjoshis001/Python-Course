n = int(raw_input())
integer_list = map(int, raw_input().split())
t=tuple(integer_list)
x=hash(t)
print (x)