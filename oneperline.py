'''OnePerLine'''
def oneper(word):
    '''oneper'''
    for i in word:
        print '"'+i+'" is in "'''+word+'''".'''
oneper(raw_input())
