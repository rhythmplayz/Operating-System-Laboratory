n = int(input("Enter the number of Processes: "))

processes = []

print("Enter the processes:")
print("In format: PID AT BT")

for i in range(n):
    temp = input().split(" ")
    processes.append((temp[0], int(temp[1]), int(temp[2]), int(temp[2]),0,0,0))

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

time_quant = int(input("Enter the time quant for preamptive: "))

while p_clpt < n:

    # To check for available process(es) in time
    while True and i < n:

        if(time >= processes[i][1]):
  
            to_clpt.append(processes[i])
            i+=1
        else:
            break



    if len(to_clpt)>0:
        
        if to_clpt[0][3]>time_quant:
            time+=time_quant

            # To check for available process(es) in time
            while True and i < n:
                if(time >= processes[i][1]):
            
                    to_clpt.append(processes[i])
                    i+=1
                else:
                    break

            temp_p = (to_clpt[0][0],to_clpt[0][1],to_clpt[0][2],to_clpt[0][3]-time_quant,to_clpt[0][4],to_clpt[0][5],to_clpt[0][6])
            to_clpt.append(temp_p)
            to_clpt.remove(to_clpt[0])
        else:
            time+=to_clpt[0][3]

            # To check for available process(es) in time
            while True and i < n:    
                if(time >= processes[i][1]):
            
                    to_clpt.append(processes[i])
                    i+=1
                else:
                    break

            ans_np.append((to_clpt[0][0],to_clpt[0][1],to_clpt[0][2],time,time-to_clpt[0][1],time-to_clpt[0][1]-to_clpt[0][2]))
            p_clpt+=1
            to_clpt.remove(to_clpt[0])
    else:
        time+=1

# Total TAT of RR
tot_np_tat = 0
# Total WT of RR
tot_np_wt = 0

for an in ans_np:
    tot_np_tat += an[4]
    tot_np_wt += an[5]

# Average TAT of RR
avg_np_tat = tot_np_tat/n
# Average WT of RR
avg_np_wt = tot_np_wt/n


# To count the current time
time = 0

# To store the completed processes
ans_p = []

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

        # Finding the process with minimum remaining BT
        mn = 10000000000000
        to_clpt.sort(key=lambda x:x[1])
        for p_t_c in to_clpt:
            if mn > p_t_c[2]:
                mn = p_t_c[2]

        # Checking is the process complete or not
        for p_t_c in to_clpt:
            if mn == p_t_c[2]:
                if p_t_c[2]<=time_quant:
                    time+=p_t_c[2]
                    p_clpt+=1
                    for p in processes:
                        if p[0]==p_t_c[0]:
                            ans_p.append((p[0],p[1],p[2],time,time-p[1],time-p[1]-p[2]))
                    to_clpt.remove(p_t_c)
                else:

                    time+=time_quant
                    to_clpt.append((p_t_c[0],p_t_c[1],p_t_c[2]-time_quant))
                    to_clpt.remove(p_t_c)
                
                break
    else:
        time+=1



# Total TAT of SjF
tot_p_tat = 0
# Total WT of SjF
tot_p_wt = 0

for an in ans_p:
    tot_p_tat += an[4]
    tot_p_wt += an[5]

# Average TAT of SjF
avg_p_tat = tot_p_tat/n
# Average WT of SjF
avg_p_wt = tot_p_wt/n

# Sort the answers in terms of PID
ans_np.sort(key=lambda x:int(x[0][1:]))
ans_p.sort(key=lambda x:int(x[0][1:]))

#print(ans_np)
#print(ans_p)
print()
print("Preemptive  RR:")
print("\tPID\tAT\tBT\tCT\tTAT\tWT")

for ans in ans_np:
    print("\t"+str(ans[0])+"\t"+str(ans[1])+"\t"+str(ans[2])+"\t"+str(ans[3])+"\t"+str(ans[4])+"\t"+str(ans[5]))
print()

print("Preemptive SJF:")
print("\tPID\tAT\tBT\tCT\tTAT\tWT")

for ans in ans_p:
    print("\t"+str(ans[0])+"\t"+str(ans[1])+"\t"+str(ans[2])+"\t"+str(ans[3])+"\t"+str(ans[4])+"\t"+str(ans[5]))
print()

print("Preemptive  RR: average TAT:",avg_np_tat,"average WT:",avg_np_wt)
print("Preemptive SJF: average TAT:",avg_p_tat,"average WT:",avg_p_wt)