reference_string = [int(x) for x in input("Enter reference string (Separated by space, example: 2 1 4): ").strip().split()]
frame_size = int(input("Enter frame size: "))

timeline = []
for i in range(frame_size):
    timeline.append([-1] * len(reference_string))

last_update_time = []
for i in range(frame_size):
    last_update_time.append([0] * len(reference_string))

hit_count = 0
miss_count = 0

for i in range(len(reference_string)):
    is_hit = False

    for j in range(frame_size):
        if i == 0:
            break

        if reference_string[i] == timeline[j][i-1]:
            hit_count += 1
            is_hit = True
            last_update_time[j][i] = i

            # Copy previous frame values
            for k in range(frame_size):
                timeline[k][i] = timeline[k][i-1]
                last_update_time[k][i] = last_update_time[k][i-1]

            last_update_time[j][i] = i
            break

    if not is_hit:
        miss_count += 1

        if i < frame_size:
            for j in range(frame_size):
                if i == 0:
                    timeline[j][i] = reference_string[i]
                    last_update_time[j][i] = i
                    break

                elif timeline[j][i-1] == -1:
                    for k in range(frame_size):
                        timeline[k][i] = timeline[k][i-1]
                        last_update_time[k][i] = last_update_time[k][i-1]

                    timeline[j][i] = reference_string[i]
                    last_update_time[j][i] = i
                    break

                else:
                    timeline[j][i] = timeline[j][i-1]

        else:
            # Copy previous frame values
            for j in range(frame_size):
                timeline[j][i] = timeline[j][i-1]
                last_update_time[j][i] = last_update_time[j][i-1]

            # Find the most recently used page
            mru_frame = last_update_time.index(
                max(last_update_time[j][i-1] for j in range(frame_size))
            ) if False else -1

            max_time = -1
            for j in range(frame_size):
                if last_update_time[j][i-1] > max_time:
                    max_time = last_update_time[j][i-1]
                    mru_frame = j

            timeline[mru_frame][i] = reference_string[i]
            last_update_time[mru_frame][i] = i

for i in range(frame_size):
    for j in range(len(reference_string)):
        if timeline[i][j] == -1:
            print("\t", end="")
        else:
            print("\t", timeline[i][j], end="")
    print()

print("Total hit:", hit_count)
print("Total miss:", miss_count)

print("Ratio hit:", hit_count / len(reference_string))
print("Ratio miss:", miss_count / len(reference_string))