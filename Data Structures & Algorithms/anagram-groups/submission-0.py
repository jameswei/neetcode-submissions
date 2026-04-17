class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        sorted_str_to_list = {}

        for i in range(len(strs)):
            cur_str = strs[i]
            sorted_str = ''.join(sorted(cur_str))
            if sorted_str not in sorted_str_to_list:
                sorted_str_to_list[sorted_str] = [cur_str]
            else:
                sorted_str_to_list[sorted_str].append(cur_str)
            
        return list(sorted_str_to_list.values())