class Solution:   # hash map. Time / Space = O(N * K * log K) / O(N * K), N = number of strings, K = max length of a string
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        cnt = defaultdict(list)
        for st in strs:
            key = tuple(sorted(st))
            cnt[key].append(st)
        return list(cnt.values())






















        # groups = defaultdict(list)
        # for st in strs:
        #     key = tuple((sorted(st)))  # Python에서 dictionary key must be immutable and hashable, thus list((sorted(st))): X
        #     # key = "".join(sorted(st))  # 둘 중 하나로 하면 됨. sorted("eat") returns ['a', 'e', 't'], so we join it back to a string
        #     groups[key].append(st)
        # return list(groups.values())
