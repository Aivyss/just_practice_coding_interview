"""
알고리즘 유형: 그리디(greedy)
idea: 각 잃어버린 사람은 자기보다 -1인 것을 선택할 수 있으면 반드시 선택하는게 최선의 책이다.
유의점: 여분이 있으면서 도난 당한 사람이 있는데 그걸 빼줘야함.

https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    remove_nums = []
    for i in lost:
        if i in reserve:
            remove_nums.append(i)

    for i in remove_nums:
        lost.remove(i)
        reserve.remove(i)

    lost_cnt = len(lost)
    answer = n - lost_cnt

    idx = 0
    for reserve_num in reserve:
        for i in range(idx, lost_cnt):
            if lost[i] + 1 == reserve_num or lost[i] - 1 == reserve_num:
                idx = i + 1
                answer += 1
                break

    return answer


# result = solution(5, [2, 4], [1, 3, 5])
# print(result)
#
# result = solution(5, [2, 4], [3])
# print(result)
#
# result = solution(3, [3], [1])
# print(result)
#
# result = solution(5, [1, 2, 3], [5])
# print(result)
#
# result = solution(5, [4, 2], [3, 5])
# print(result)

result = solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12])
print(result)
