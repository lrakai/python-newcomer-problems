def list_uniqueness(the_list):
    '''
    Return a dictionary with two key-value pairs:
      1. The key 'list_length' stores the lenght of the_list as its value.
      2. The key 'unique_items' stores the number of unique items in the_list as its value.
    Arguments
    the_list: A list
    Examples
    l = [1, 2, 2, 4]
    dictionary = list_uniqueness(l)
    print(dictionary['list_length']) # prints 4
    print(dictionary['unique_items']) # prints 3
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will create the required dictionary
    

    # ====================================
    # Do not change the code after this
    
    return dictionary


if __name__ == '__main__':
    l = [1, 2, 2, 4]
    dictionary = list_uniqueness(l)
    print(dictionary['list_length'])
    print(dictionary['unique_items'])