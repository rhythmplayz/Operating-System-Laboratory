n = int(input("Enter the number of Processes: "))

processes = []

print("Enter the processes:")
print("In format: PID AT BT Priority")

for i in range(n):
    temp = input().split()
    processes.append([temp[0], int(temp[1]), int(temp[2]), int(temp[3]), 0, 0, 0, int(temp[2])])

time_quant = int(input("Enter the time quant for preemptive: "))

# Sorting the processes based on Arrival Time (AT)
processes.sort(key=lambda x: x[1])

time = 0
ans_p = []
p_clpt = 0
to_clpt = []
i = 0

while p_clpt < n:
    # Add all processes that have arrived by current time
    while i < n and processes[i][1] <= time:
        to_clpt.append(processes[i])
        i += 1

    if len(to_clpt) > 0:
        # Sort ready queue by highest priority (lowest priority number)
        to_clpt.sort(key=lambda x: x[3])
        
        # Pick the highest priority process
        curr = to_clpt.pop(0)
        
        # Execute for minimum of time_quant or remaining burst time
        exec_time = min(time_quant, curr[7])
        time += exec_time
        curr[7] -= exec_time

        # Check for new processes that arrived during execution
        while i < n and processes[i][1] <= time:
            to_clpt.append(processes[i])
            i += 1

        # If process finishes
        if curr[7] == 0:
            p_clpt += 1
            ct = time
            tat = ct - curr[1]
            wt = tat - curr[2]
            ans_p.append((curr[0], curr[1], curr[2], curr[3], ct, tat, wt))
        else:
            to_clpt.append(curr)
    else:
        time += 1

# Calculate Totals
tot_p_tat = sum(ans[5] for ans in ans_p)
tot_p_wt = sum(ans[6] for ans in ans_p)

# Calculate Averages
avg_p_tat = tot_p_tat / n
avg_p_wt = tot_p_wt / n


ans_p.sort(key=lambda x: int(''.join(filter(str.isdigit, x[0]))) if any(c.isdigit() for c in x[0]) else x[0])

print()
print("Average TAT:", avg_p_tat, "\t", "Average WT:", avg_p_wt)

print()
print("Preemptive Priority:")
print("\tPID\tAT\tBT\tPriority\tCT\tTAT\tWT")

for ans in ans_p:
    print("\t" + str(ans[0]) + "\t" + str(ans[1]) + "\t" + str(ans[2]) + "\t" + str(ans[3]) + "\t\t" + str(ans[4]) + "\t" + str(ans[5]) + "\t" + str(ans[6]))