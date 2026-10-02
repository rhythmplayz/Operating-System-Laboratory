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

print()
print()
print("Sequence: ",head,end="")

for i in range(n):
    if requests[i][0] == head:
        requests[i][1] = 1
        break

total_no_of_seek_operations = 0

for i in range(n):
    if requests[i][1] == 0:
        movement = abs(head-requests[i][0])
        total_no_of_seek_operations += movement
        head = requests[i][0]
        requests[i][1] = 1
        print(" ->",head,end="")
print()
print()

print("Total no of seek operations:",total_no_of_seek_operations)
print()
print()