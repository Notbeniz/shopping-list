items=[]
def show_menu():
    print("""
            Help : Menu
            New : New Item
            Items : All List
            Del : Delete Item
            End : Quit
        """)

def add_item():
    while True:
        new_item=input('>>').capitalize()
        if new_item!='Done':
            items.append(new_item)
            print(f'You have {len(items)} items in your list.')
        elif new_item =='Done':
            list_items=', '.join(items)
            print(f'Your items are: {list_items}.')
            break

def del_item():
    show_items() 
    item=input('>>').capitalize()
    if item in items:
        delete_req=input(f'Do you want delete {item}? Y/N ').capitalize()
        if delete_req=='Y':
            if item in items:
                items.remove(item)
                show_items()
            else:
                print(f'You dont have {item} in your list!')
        elif delete_req=='N':
            print(f'You Have {len(items)} Items In Your List.')
        else:
            delete_req=input(f'Do You Want Delete {item}? Y/N ').capitalize()


    
def show_items():
    # print('show_item')
    if items==[]:
        print('Your list  is empty!!')
    else:
        list_items=', '.join(items)
        print(f'Your items are: {list_items}.')   

show_menu()
while True:
    
    req=input('>').capitalize()

    if req=='Help':
        show_menu()
    elif req=='New':
        add_item()
    elif req=='Items':
        show_items()
    elif req=='Del':
        del_item()
    elif req=='End':
        break

