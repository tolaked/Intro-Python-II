# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,items=[]):
        self.name = name
        self.description = description
        self.items=items
        self.e_to = None
        self.s_to = None
        self.n_to = None
        self.w_to = None
    
    # def add_item(self, item):
    #     self.items.append(item)
    # def allitems(self):
    #     if self.items == None:
    #         print(f'there are no items in {self.name}')
    #     else:
    #         output=f'current room: {self.name} {self.description}'

    #         for i in self.items:
    #             output+=f'Available items are: [{i}]'