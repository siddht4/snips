import os
_path='' # path of the directory to be split 
_file_list=os.listdir(_path)

# function to split or slice the list into two
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
    
_a1,_a2=split_list(_file_list)  # call function and assign the split value/half values to a1,a2 ,  
print(_a2)
