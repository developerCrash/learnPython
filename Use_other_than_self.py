class abc:
    def __init__(anil):
        anil.my_list = []  
    def push(anil, item):
        anil.my_list.append(item)
    def display(anil):
        print(anil.my_list)
        
a = abc()
a.push(10)
a.display()
