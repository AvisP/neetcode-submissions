class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        arr = numbers

        while l<r:
            # print(l, r)
            if arr[l] + arr[r] == target:
                return [l+1,r+1]
            elif arr[l] + arr[r] < target:
                l = l + 1
            elif arr[l] + arr[r] > target:
                r = r -1

        return []