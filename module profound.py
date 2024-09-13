myitems = []
check_num = 1
def add_item(itemName, itemCost):
    global myitems
    myitems.append([itemName, itemCost])

def  print_receipt():
    global check_num, myitems
    if myitems:
        print(f'Check {check_num}. Number of items: {len(myitems)}')
        for i in myitems:
            print(i[0], '-', i[1])
        print(f'Total: {sum([i[1] for i in myitems])}')
        print('-----')
        check_num += 1
    myitems.clear()


add_item('Keyboard', 100)
print_receipt()

add_item('Mouse', 70)
print_receipt()
print_receipt()

add_item('Screen', 15)
add_item('Screen', 15)
add_item('Pen', 5)
print_receipt()

add_item('Screen', 15)
add_item('Screen', 15)
# Cancel