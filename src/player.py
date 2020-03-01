# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name,current_room,items=[]):
        self.name = name
        self.current_room = current_room
        self.items=items
    
    def add_item(self,item):
        self.items.append(item)
    
    def allitems(self):
        if self.items == None:
            print(f'there are no items in {self.name}')
        else:
            pass

            for i in self.items:
                output=f'Available items are: {i}'
                return output