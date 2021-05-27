list1=[6,9,1,3,5,2]
list1.sort()
print(list1)
# 2 Task
# 3 Task
t=(2.3, 4.5, 6.7, 8.9, 0.1, 1.2, 3.2, 6.5, 7.1, 2.0)
print(max(t))
print(min(t))
# 4 Task
list = ["Earth", "Russia", "Moscow"]
location=list[0]
n=len(list)

for i in range(1, n):
    location=location+"->" + list[i]
print(location)
# 5 Task
string= '/bin:/usr/bin:/usr/local/bin'.split(":")
print(string)
# 6 Task
summ=str(0)
for i in range(0, 101):
    if 0==i%7:
        summ= summ + " " +str(i)
print(summ)