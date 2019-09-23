def append(the_list, item):
    '''
    Append item to the_list
    Arguments
    the_list: A list
    item: The item to append to the_list
    Examples
    l = [1, 2, 3]
    append(l, 4)
    print(l) # prints [1, 2, 3, 4]
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Fix the code below to correctly append item to the_list
    new_list = the_list
    new_list = new_list + [item]
    the_list = new_list

    # ====================================
    # Do not change the code after this


if __name__ == '__main__':
    l = [1, 2, 3]
    append(l, 4)
    print(l)