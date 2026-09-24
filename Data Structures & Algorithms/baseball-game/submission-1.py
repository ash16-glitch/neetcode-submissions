class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for i in operations:
            if i =='+':
                records.append(records[-1]+records[-2])
            elif i =='D':
                    records.append(records[-1]*2)
            elif i =='C':
                    records.pop()
            else:
                records.append(int(i))
        total_sum = sum(records)
        return total_sum
