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

        
class Backbone:
    '''
    list of dict 
    parts as dict collected in a list with order of appending
    '''

    def __init__(self, ):
        self.backbone = []

    def append_part(self, part):
        '''
        
        '''
        self.backbone.append(part) 
        return self.backbone

    def return_backbone(self):
        return self.backbone

    def print_backbone(self):
        '''
        
        '''
        print(self.backbone)

part1 = Part('Promoter1',1,'SO:2253254236',"Omar's Promoter")
part1_dict = part1.part_di()
# print(part1_dic)

part2 = Part('Promoter2',1,'SO:432436',"Tom's Promoter")
part2_dict = part2.part_di()

part3 = Part('RDS',1,'SO:923659328567',"Ahmed's RBS")
part3_dict = part3.part_di()
# print(part3_dict)

part4 = Part('CDS',1,'SO:87265923869328567',"James's CDS")
part4_dict = part4.part_di()

part5 = Part('Terminator',1,'SO:87265923869328567',"Tom's CDS")
part5_dict = part5.part_di()

backbone1 = Backbone()
backbone1.append_part(part1_dict)
backbone1.append_part(part2_dict)
backbone1.append_part(part3_dict)
backbone1.append_part(part4_dict)
backbone1.append_part(part5_dict)
backbone1.print_backbone()


