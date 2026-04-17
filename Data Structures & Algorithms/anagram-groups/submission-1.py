class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
 
        char_count_to_list = {}

        for cur_str in strs:
            # 26 lower case characters
            count_of_all_lower_case_chars = [0] * 26
            for c in cur_str:
                count_of_all_lower_case_chars[ord(c)-ord('a')] += 1
            tpl = tuple(count_of_all_lower_case_chars)
            if tpl not in char_count_to_list:
                char_count_to_list[tpl] = []
            char_count_to_list[tpl].append(cur_str)
        return list(char_count_to_list.values())
            
            