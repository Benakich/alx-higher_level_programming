#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (my_list is None) | (idx is None) | (element is None)\
            | (idx < 0) | (idx >= len(my_list)):
        return my_List
    listcpy = my_list.copy()
    listcpy[idx] = element
    return listcpy
