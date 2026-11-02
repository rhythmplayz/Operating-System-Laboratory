n = int(input("Enter the number of Processes: "))

processes = []

print("Enter the processes:")
print("In format: PID AT BT Priority")

for i in range(n):
    temp = input().split(" ")
    processes.append((temp[0], int(temp[1]), int(temp[2]), int(temp[3]),0,0,0))

#non-preemptive priority scheduling
# Sorting the processes based on AT
processes.sort(key = lambda x:x[1])

# To count the current time
time = 0

# To store the completed processes
ans_np = []

# Total completed processes
p_clpt = 0

# This is ready queue
to_clpt = []

# To check any available process(es)
i = 0

while p_clpt < n:

    # To check for available process(es) in time
    while True and i < n:
        if(time >= processes[i][1]):
  
            to_clpt.append(processes[i])
            i+=1
        else:
            break


    if len(to_clpt)>0:

        # Finding the process with highest priority (lowest priority number)
        mn = 10000000000000
        to_clpt.sort(key=lambda x:(x[3], x[1]))

        process = to_clpt[0]

        time+=process[2]
        p_clpt+=1

        ans_np.append((process[0],process[1],process[2],process[3],time,time-process[1],time-process[1]-process[2]))
        to_clpt.remove(process)
    else:
        time+=1

# Total TAT of non-preemptive priority
tot_np_tat = 0
# Total WT of non-preemptive priority
tot_np_wt = 0

for an in ans_np:
    tot_np_tat += an[4]
    tot_np_wt += an[5]

# Average TAT of non-preemptive priority
avg_np_tat = tot_np_tat/n
# Average WT of non-preemptive priority
avg_np_wt = tot_np_wt/n

# Sort the answers in terms of PID
ans_np.sort(key=lambda x:int(x[0][1:]))

print()
print("Average TAT:",avg_np_tat,"\t","Average WT:",avg_np_wt)

print()
print("Non-preemptive Priority:")
print("\tPID\tAT\tBT\tPriority\tCT\tTAT\tWT")

for ans in ans_np:
    print("\t"+str(ans[0])+"\t"+str(ans[1])+"\t"+str(ans[2])+"\t"+str(ans[3])+"\t\t"+str(ans[4])+"\t"+str(ans[5])+"\t"+str(ans[6]))
print()