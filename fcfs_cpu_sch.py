n = int(input("Enter the number of processes: "))

processes = list()

print("Enter the processes (In format --> PID AT BT): ")

for i in range(n):
    PID, AT, BT = input().split(" ")
    processes.append( (PID,int(AT),int(BT)) )

processes.sort(key = lambda x : x[1])

crnt_tm = 0

full_cal = list()

tot_TAT = 0
tot_WT = 0

for p in processes:
    if crnt_tm < p[1]:
        crnt_tm = p[1]

    CT = crnt_tm + p[2]
    TAT = CT - p[1]
    WT = TAT - p[2]

    tot_TAT += TAT
    tot_WT += WT

    crnt_tm = CT

    full_cal.append((p[0], p[1], p[2], CT, TAT, WT))


avg_TAT = tot_TAT/n
avg_WT = tot_WT/n

for fc in full_cal:
    print(fc)

print("Average TAT:",avg_TAT)
print("Average WT:",avg_WT)


