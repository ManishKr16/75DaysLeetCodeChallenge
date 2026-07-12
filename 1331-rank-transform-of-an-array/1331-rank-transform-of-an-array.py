class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [ranks[x] for x in arr]
        