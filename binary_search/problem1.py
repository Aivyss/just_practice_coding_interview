"""
알고리즘 유형: 이진 탐색 (binary search)
idea: 점수의 최소 최대를 잡고 점수 조건을 넘는 것을 이진 탐색으로 추려낸 뒤 나머지 조건에 일치하는 것을 filtering

효율성 해결을 하려면 다른 방식이 필요한 것 같다.
지금의 로직에서 dictionary를 이용해서 출일 수 있나 봤으나 runtime error 발생 및 일부 케이스에서 더 느림

낮은 레벨로 책정됐으나 쉬운 문제인지 잘 모르겠음;;

https://school.programmers.co.kr/learn/courses/30/lessons/72412
"""


def predicate(q, entry):
    return (q[0] == '-' or q[0] == entry[0]) \
           and (q[1] == '-' or q[1] == entry[1]) \
           and (q[2] == '-' or q[2] == entry[2]) \
           and (q[3] == '-' or q[3] == entry[3])


def solution(info, query):
    entries = []
    for elem in info:
        language, position, rank, food, score = map(str, elem.split())
        entries.append((language, position, rank, food, int(score)))

    queries = []
    for elem in query:
        language, position, rank, food_and_score = elem.split(' and ')
        queries.append((language, position, rank, food_and_score.split()[0], int(food_and_score.split()[1])))

    entries.sort(key=lambda element: element[4])

    indices = []
    for q in queries:
        left_idx = 0
        right_idx = len(entries) - 1
        query_score = q[4]
        result_idx = -1
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            score = entries[mid_idx][4]

            if query_score > score:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
                result_idx = mid_idx

        indices.append(result_idx)

    answer = []
    for idx in range(len(queries)):
        if indices[idx] != -1:
            valid_entries = entries[indices[idx]:]
            q = queries[idx]
            temp = list(filter(lambda x: predicate(q, x), valid_entries))
            answer.append(len(temp))
        else:
            answer.append(0)

    return answer