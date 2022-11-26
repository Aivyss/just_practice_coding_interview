"""
최대의 회의실 사용 수를 구하라 (그리디)

첫째줄 스케줄의 갯수
둘째줄부터 스케줄들의 시간이 각 라인별로 (시작시, 끝시)로 주어짐.
같은 시간대에서 동시에 사용할 수 없고, 각 회의는 끝나는 시간인 즉시 다른 회의로 이어서 할 수 있다. 예를들어 (1, 4) 가 끝날 때 바로 (4, 5)가 가능

주어진 스케줄 내에서 최대한 회의실을 사용할 수 있는 횟수를 구할 것.

알고리즘 유형: greedy (그리디)
idea: 그리디 유형임을 파악하고, 잘 정렬만 하면 된다. 그리디인지 아닌지 아는게 제일 중요할 듯
"""
from snippets.testing import Solution


def solution():
    # inputs
    n = int(input())
    schedules = [tuple(map(int, input().split())) for _ in range(n)]

    # process
    schedules.sort(key=lambda x: (x[1], x[0]))
    end_time = 0
    cnt = 0
    for s, e in schedules:
        if s >= end_time:
            end_time = e
            cnt += 1

    print(cnt)


Solution("problem_5", solution, 6).measure()
