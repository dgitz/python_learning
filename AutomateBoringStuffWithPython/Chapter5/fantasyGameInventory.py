def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for item,count in inventory.items():
        itemTotal += count
        print(str(count) + ' ' + item)
    print('Total number of Items: ' + str(itemTotal) + '\n')

def addInventory(items,inventory):
    for item in items:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory


inventory = {'gold coin': 42, 'rope': 1}
displayInventory(inventory)

newItems = ['gold coin','dagger','gold coin','gold coin', 'ruby']
inventory = addInventory(newItems,inventory)
displayInventory(inventory)