'''reverse word'''
def rev(word):
    '''reverse'''
    fff = word.split()
    fff.reverse()
    fff = ' '.join(fff)
    print fff
rev(raw_input())
