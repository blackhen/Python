'''PostQuiz1Round1dot1_Sandwich'''
def sanwich(len_string, string_1, string_2):
    '''print string_1+space+string_2'''
    print string_1+' '*(len_string-len(string_1+string_2))+string_2
sanwich(input(), raw_input(), raw_input())
