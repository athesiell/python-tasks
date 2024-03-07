from typing import List

def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    table = []
    for i in range(row_start, row_end + 1):
        row = []
        for j in range(column_start, column_end + 1):
            row.append(i * j)
        table.append(row)
    return table

row_start = 2
row_end = 4
column_start = 3
column_end = 7 

print(check(row_start, row_end, column_start, column_end))