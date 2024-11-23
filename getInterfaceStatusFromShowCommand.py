my_str = '''interface protocol status
ge-0/0/0  ospf      up
ge-1/0/1  rsvp      down
'''

def get_interface_status(my_str):
    interface_dict = {}
    ind_lines = my_str.splitlines()
    
    for i in ind_lines[1:]:
        column = i.split()
        #print(column)
        interface_dict[column[0]] =  column[2]
        
    print(interface_dict)
    
    
get_interface_status(my_str)
