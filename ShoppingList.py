items=[]
while True:
    print("""
            Help : Menu
            New : New Item
            Items : All List
            Del : Delete Item
            End : Quit
        """)
    req=input('> ').capitalize()

    if req=='New' :
        while True:
            item=input('>> ').capitalize()
            if item!='Done':
                items.append(item)
                print(f'You Have {len(items)} Items In Your List.')
            if item=='Done':
                list_item=', '.join(items)
                print(f'Your Items Are : {list_item}.')
                break
    elif req=='Items' :
            if items==[]:
                print('Your List Item Is Empty! ')
            else:
                print(f'Your Items Are : {list_item}.')
    elif req=='Del' :
        print(f'Your Items Are : {list_item}.')
        delete_item=input('>>>').capitalize()
        delete_req=input(f'Do You Want Delete {delete_item}? Y/N : ').capitalize()
        if delete_req=='Y':
            items.remove(delete_item)
            print(f'{delete_item} Deleted!! You have You Have {len(items)} Items In Your List.')
            print(f'Your Items Are : {list_item}.')
        elif delete_req=='N':
            print(f'You Have {len(items)} Items In Your List.')
        else :
            del_req=input(f'Do You Want Delete {delete_item}? Y/N : ').capitalize()

    elif req=='End':
        break