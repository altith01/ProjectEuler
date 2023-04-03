# Under The Rainbow

from time import time_ns
start_time = time_ns()

prob_array = [[0]*7 for _ in range(20)]
prob_array[0][0] = 1

total_balls = 70

for draw in range(len(prob_array)-1):
    for color_count in range(len(prob_array[draw])):
        # if prob_array[draw][color_count] == 0:
        #     break
        if color_count == 6:
            prob_array[draw+1][color_count] += prob_array[draw][color_count]
        else:
            prob_array[draw+1][color_count] += (10*(color_count+1)-(draw+1))/(total_balls-(draw+1))*prob_array[draw][color_count]
            prob_array[draw+1][color_count+1] += (10*(6-color_count))/(total_balls-(draw+1))*prob_array[draw][color_count]

weighted_avg = sum((i+1)*prob_array[-1][i] for i in range(len(prob_array[-1])))

elapsed = (time_ns() - start_time) / 1000000
print(weighted_avg)
print(elapsed, "ms")
