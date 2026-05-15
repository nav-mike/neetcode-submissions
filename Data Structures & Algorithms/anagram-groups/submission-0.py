class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            val = "".join(sorted(s))
            array = hashMap.get(val, [])
            array.append(s)
            hashMap[val] = array
            
        
        return list(hashMap.values())