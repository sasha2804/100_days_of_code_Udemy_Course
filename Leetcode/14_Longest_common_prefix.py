from pyparsing import stringStart


strs = ["flolllweöllllllllr","flow","floght"]

strs = [""]


# strs = ["ab", "a", "aaaaaaa"]

strs = ["cir","car"]


class Solution:
  
    def longestCommonPrefix(self, strs):
        str_return = ""
        ind_1 = 0
        symbol = ""      

        # if len(strs[0]) == 0:
        #     trig = False
        #     return "00000"
        
        # min length of the list element
        length = len(strs[0])
        for i in strs:
            if len(i) < length:
                length = len(i)
        print('min length: ',length)
        
        # cut string to ming length
        for i in range(len(strs)):
            strs[i] = strs[i][:length]        
        print(strs)



        for i in range(len(strs[0])):
            symbol = strs[ind_1][i]

            for j in range(1,len(strs)):
                if symbol != strs[j][i]:
                    symbol = ""
                    return str_return                    
                    # break


            str_return += symbol
        return str_return

         # while trig:
        #     symbol = strs[ind_1][ind_2]

        #     for i in range(1, len(strs)):
        #         if symbol != strs[i][ind_2]:
        #             symbol = ""
        #             trig = False
        #             break  

        #     str_return += symbol
        #     ind_2 += 1
        # return str_return


solution = Solution()

print(solution.longestCommonPrefix(strs))