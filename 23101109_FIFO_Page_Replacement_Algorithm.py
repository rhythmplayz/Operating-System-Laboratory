reference_string = [int(x) for x in input("Enter reference string (Separated by space, example: 2 1 4): ").strip().split(" ")]
frame_size = int(input("Enter frame size: "))

timeline = []
for i in range(frame_size):
    timeline.append([-1]*len(reference_string))

last_update_time = []
for i in range(frame_size):
    last_update_time.append([0]*len(reference_string))

hit_count = 0
miss_count = 0

for i in range(len(reference_string)):
    is_hit = False
    mx = -1
    for j in range(frame_size):
        if i == 0:
            break
        if mx < last_update_time[j][i-1]:
            mx = last_update_time[j][i-1]
        if reference_string[i] == timeline[j][i-1]:
            hit_count += 1
            is_hit = True
            break
    if is_hit:
        for j in range(frame_size):
            last_update_time[j][i] = last_update_time[j][i-1]+1
            timeline[j][i]=timeline[j][i-1]
    else:
        miss_count += 1
        if i<frame_size:
            for j in range(frame_size):
                if i==0:
                    timeline[j][i] = reference_string[i]
                    last_update_time[j][i] = 1
                    break
                elif timeline[j][i-1]==-1:
                    timeline[j][i] = reference_string[i]
                    last_update_time[j][i] = 1
                    break
                else:
                    last_update_time[j][i] = last_update_time[j][i-1]+1
                    timeline[j][i]=timeline[j][i-1]
        else:
            for j in range(frame_size):
                if last_update_time[j][i-1]==mx:
                    timeline[j][i] = reference_string[i]
                    last_update_time[j][i] = 1
                else:
                    last_update_time[j][i] = last_update_time[j][i-1]+1
                    timeline[j][i]=timeline[j][i-1]

for i in range(frame_size):
    for j in range(len(reference_string)):
        if timeline[i][j]==-1:
            print("\t",end="")
        else:
            print("\t",timeline[i][j],end="")
    print()

print("Total hit:",hit_count)
print("Total miss:",miss_count)

print("Ratio hit:",hit_count/len(reference_string))
print("Ratio miss:",miss_count/len(reference_string))
