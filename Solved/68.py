# Magic 5-gon ring
# Sums bounded from 14-18
# 10 used only once

from itertools import combinations
from time import time_ns

def build_it(in_seq, out_seq):
    answer = ""
    in_seq += in_seq
    for i in range(5):
        answer += str(out_seq[i]) + str(in_seq[i]) + str(in_seq[i+1])
    return answer


def find_it(start: int, remaining_in: set, remaining_out: set, in_seq: list, out_seq: list):
    if start:
        combos = [x for x in combinations(remaining_in, 2) if sum(x)+start == LINE_SUM]
        best = ""
        for combo in combos:
            best = max(
                best,
                find_it(0, remaining_in.difference(set(combo)), remaining_out, [combo[0], combo[1]], [start]),
                find_it(0, remaining_in.difference(set(combo)), remaining_out, [combo[1], combo[0]], [start])
            )
        return best
    if len(remaining_in) == 0:
        return build_it(
            in_seq, out_seq + list(remaining_out)
        ) if list(remaining_out)[0] + int(in_seq[0]) + int(in_seq[-1]) == LINE_SUM else ""
    else:
        goal = LINE_SUM - int(in_seq[-1])
        best = ""
        for inside in remaining_in:
            for outside in remaining_out:
                if outside + inside == goal:
                    best = max(
                        best,
                        find_it(
                            0, 
                            remaining_in.difference(set([inside])), 
                            remaining_out.difference(set([outside])), 
                            in_seq + [inside], 
                            out_seq + [outside]
                        ),
                    )
        return best

starttime = time_ns()

inside_set = set(range(1,6))
outside_set = set(range(6,11))
LINE_SUM = (sum(inside_set) + 55) // 5 #14

answer = find_it(6, inside_set, outside_set.difference(set([6])), "", "")
elapsed = (time_ns() - starttime)/1000000
print(answer)
print(elapsed, "ms")