import sys
import time


class Solution:
    def __init__(self, file_name: str, solution_func, loop_cnt: int):
        self.file_name = file_name
        self.solution_func = solution_func
        self.loop_cnt = loop_cnt

    def measure(self):
        for i in range(self.loop_cnt):
            run_file_name = f'{self.file_name}_{i + 1}.txt'
            print(f"=====[{run_file_name}]=====")

            sys.stdin = open(run_file_name, 'rt')
            start_time = time.time()
            self.solution_func()
            end_time = time.time()

            print()
            print(f"{end_time - start_time:.5f} sec")
