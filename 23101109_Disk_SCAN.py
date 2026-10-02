print()
print()
print()

n = int(input("Enter the number of requests: "))

requests = []

for i in range(n):
    msg = "Enter the no."+str(i+1)+" request: "
    request = int(input(msg))
    requests.append([request,0])

head = int(input("Enter the head position: "))

dr = input("Enter direction (L/l for left and R/r for right): ").lower()

dr_min = min(requests, key= lambda x:x)
dr_max = max(requests, key= lambda x:x)

print()
print()


total_no_of_seek_operations = (abs(dr_min[0]-head)+abs(dr_min[0]-dr_max[0])) if dr == 'l' else (abs(dr_max[0]-head)+abs(dr_min[0]-dr_max[0]))


print("Sequence: ",head,end="")
requests.sort(key=lambda x:x)
idx = -1
for i in range(n):
    if requests[i][0]>=head:
        idx = i
        break

if dr == 'l':
    for i in range(idx-1,-1,-1):
            head = requests[i][0]
            print(" ->",head,end="")
    for i in range(idx,n):
        if requests[i][0]==head:
            continue
        else:
            head = requests[i][0]
            print(" ->",head,end="")
else:
    for i in range(idx,n):
            if requests[i][0]==head:
                continue
            else:
                head = requests[i][0]
                print(" ->",head,end="")
    for i in range(idx-1,-1,-1):
                head = requests[i][0]
                print(" ->",head,end="")
        
print()
print()

print("Total no of seek operations:",total_no_of_seek_operations)
print()
print()