class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for path in paths:
            p = path.split()
            root = p[0]
            for file in p[1:]:
                idx = file.find("(")
                fn, content = file[:idx], file[idx:]
                dic[content].append(root + "/" + fn)
        return [dic[key] for key in dic if len(dic[key]) > 1]