class Solution:
    def leaders_in_array(self, nums: list[int]) -> list[int]:
        n = len(nums)

        if n == 0:
            return []

        leaders = []
        max_right = nums[n - 1]


        leaders.append(nums[n - 1])

        for index in range(n - 2, -1, -1):

            if nums[index] >= max_right:
                leaders.append(nums[index])


            max_right = max(max_right, nums[index])

        leaders.reverse()

        return leaders


if __name__ == "__main__":
    nums = [10, 22, 12, 3, 0, 6]

    solution = Solution()
    leaders = solution.leaders_in_array(nums)

    print(*leaders)