n = int(input("Enter the number of Processes: "))

processes = []

print("Enter the processes:")
print("In format: PID AT BT")

for i in range(n):
    temp = input().split(" ")
    processes.append((temp[0], int(temp[1]), int(temp[2])))

processes.sort(key = lambda x:x[1])

time = 0

ans_np = []

p_clpt = 0

to_clpt = []

i = 0

while p_clpt < n:

    while True and i < n:

        if(time >= processes[i][1]):
  
            to_clpt.append(processes[i])
            i+=1
        else:
            break
    if len(to_clpt)>0:

        mn = 10000000000000
        to_clpt.sort(key=lambda x:x[1])
        for p_t_c in to_clpt:
            if mn > p_t_c[2]:
                mn = p_t_c[2]
        for p_t_c in to_clpt:
            if mn == p_t_c[2]:
                time+=mn
                p_clpt+=1
                ans_np.append((p_t_c[0],p_t_c[1],p_t_c[2],time,time-p_t_c[1],time-p_t_c[1]-p_t_c[2]))
                
                to_clpt.remove(p_t_c)
                
                break
    else:
        time+=1

tot_np_tat = 0
tot_np_wt = 0

for an in ans_np:
    tot_np_tat += an[4]
    tot_np_wt += an[5]

avg_np_tat = tot_np_tat/n
avg_np_wt = tot_np_wt/n


time_quant = int(input("Enter the time quant for preamptive: "))


time = 0

ans_p = []

p_clpt = 0

to_clpt = []

i = 0

while p_clpt < n:

    while True and i < n:

        if(time >= processes[i][1]):
  
            to_clpt.append(processes[i])
            i+=1
        else:
            break

    if len(to_clpt)>0:

        mn = 10000000000000
        to_clpt.sort(key=lambda x:x[1])
        for p_t_c in to_clpt:
            if mn > p_t_c[2]:
                mn = p_t_c[2]

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



tot_p_tat = 0
tot_p_wt = 0

for an in ans_p:
    tot_p_tat += an[4]
    tot_p_wt += an[5]

avg_p_tat = tot_p_tat/n
avg_p_wt = tot_p_wt/n

print(ans_np)
print(ans_p)
print("Non-preamptive: average TAT:",avg_np_tat,"average WT:",avg_np_wt)
print("Preamptive: average TAT:",avg_p_tat,"average WT:",avg_p_wt)