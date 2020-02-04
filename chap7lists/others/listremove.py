def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']
    #del food[1]#delete element at index 1
    # Display the list.
    print('Here are the items in the food list:')
    print(food)
    # Get the item to change.
    item = input('Which item should I remove? ')
    
    try:
        # Remove the item.
        food.remove(item)
        # Display the list.
        print('Here is the revised list:')
        print(food)
    
    except ValueError:
        print('That item was not found in the list.')
    """
    except Exception as e:
        print('That item was not found in the list.',e)
    """
    # finally:
    #     del food
    #     print('Food is deleted')
    # # Call the main function.
main()