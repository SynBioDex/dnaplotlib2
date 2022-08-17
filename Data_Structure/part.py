class Part:
    '''
    
    
    '''
    def __init__(self, part_type, orientation, so_term, name):
        self.part_type = part_type
        self.orientation = orientation
        self.so_term = so_term
        self.name = name
        self.part_list = []
        self.part_dict = {}
    
    def part_li(self):
        '''
        Parameters: 
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))    

        so_term -> ontology
        name -> string    
        
        '''
        self.part_list.append(self.part_type)
        self.part_list.append(self.orientation)
        self.part_list.append(self.so_term)
        self.part_list.append(self.name)
        # print(self.part_list)

        return self.part_list
    
    def part_di(self):
        '''
        
        Parameters: 
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))    

        so_term -> ontology
        name -> string  
        '''
        self.part_dict['part_type'] = self.part_type
        self.part_dict['orientation'] = self.orientation
        self.part_dict['so_term'] = self.so_term
        self.part_dict['name'] = self.name
        # print(self.part_dict)
        
        return self.part_dict
    
part1 = Part('Promoter',1,'SO:432436','Ahmed')
output1 = part1.part_li()
output2 = part1.part_di()
print(output1, output2)
    
    