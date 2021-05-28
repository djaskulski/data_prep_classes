#!/usr/bin/env python
# coding: utf-8

# In[68]:


import random


# In[69]:


def list_manipulator() -> None:
    """ 
    i) Modify below code to be able to repeat all above steps 
       to get the same results each time
    """
    
    print("a) Create a list with 5 fruit names")
    fruit_names = ["Apple", "Pear", "Blueberry", "Raspberry", "Strawberry"]
    print(fruit_names, "\n")

    print("b) Extend the fruit_names list with 2 vegatables")
    for i in ["Tomato", "Onion"]:
        fruit_names.append(i)
    print(fruit_names, "\n")

    print("c) Shuffle the list")
    random.shuffle(fruit_names)
    print(fruit_names, "\n")

    print("d) Find the position of first vegetable") 
    index1 = fruit_names.index("Tomato")
    index2 = fruit_names.index("Onion")
    if index1 > index2:
        print(index2, "\n")
    else:
        print(index1, "\n")

    print("e) Remove one fruit")
    fruit_names.remove("Pear")

    print("f) Print the (final) result")
    print(fruit_names, "\n")

    print("g) Sort the list in alphabetical order")
    fruit_names.sort()
    
    print("h) Print each element of a list using a loop")
    for i in fruit_names:
        print(i)


# In[70]:


def tuple_manipulator() -> None:
    """
    # Pair up above lists
    # Using a loop unpack the tuple into variables: first_el, secodn_el
    # Print the pair position and variables using f-string.
        # Example:
        # "Index of a3 and b3 is equal 2"
    """
    
    first_list = ["a" + str(number) for number in range(1, 10)]
    second_list = ["b" + str(number) for number in range(1, 10)]
    print("Lists: \n", *first_list, "\n", *second_list, "\n")
    
    
    paired_list = list(zip(first_list, second_list))
    print("paired lists: ", paired_list, "\n")

    
    index_counter = 0
    for i in paired_list:
        first_el, secodn_el = i
        print(f"Index of {first_el} and {secodn_el} is equal {index_counter}")
        index_counter += 1


# In[71]:


def sets_manipulator() -> None:
    """
    # I thought this was about all about Sets - not lists.
    # Find the overlapping names in above lists
    # Print number of "duplicated" names
    # Find and print the union of above lists and length
    # Find and print the difference between lists and length
    """
    
    fake_names_1 = ['Sherry', 'Mary', 'Matthew', 'Danielle', 'Jeffrey', 'Lauren', 
                  'Keith', 'Carlos', 'Monique', 'Laura', 'Jared', 'Valerie', 'Juan', 
                  'Christopher', 'Erica', 'Dawn', 'Joshua', 'Brandon', 'Stephanie']

    fake_names_2 = ['Andre', 'Anthony', 'Lauren', 'Douglas', 'Jonathan', 'Richard', 
                    'Alyssa', 'Vincent', 'Travis', 'Clifford', 'Jerry', 'Justin',
                    'Matthew', 'Jared', 'Erica']

    fake_names_1 = set(fake_names_1)
    fake_names_2 = set(fake_names_2)
    print("list_1: ", *fake_names_1, "\n", "\nlist_2: ", *fake_names_2, "\n")
    
    
    intersected = fake_names_1.intersection(fake_names_2)
    print("intersected: ", intersected)
    print("len of intersected: ", len(intersected), "\n")

    united = fake_names_1.union(fake_names_2)
    print("united: ", united)
    print("len of united: ", len(united), "\n")

    differenced = fake_names_1.symmetric_difference(fake_names_2)
    print("differenced: ", differenced)
    print("len of differenced: ", len(differenced))


# In[72]:


def main():
    
    list_manipulator()
    tuple_manipulator()
    sets_manipulator()


# In[73]:


if __name__ == "__main__":
    main()


# In[74]:


#get_ipython().system('jupyter nbconvert --to python "lists&sets.ipynb"')

