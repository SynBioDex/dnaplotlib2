'''
test case for part class functions
'''
import dnaplotlib2 as dpl

def test_part_di():
    '''
    function to test the return of part_di function
    '''
    part_1 = dpl.Part(part_type="Promoter", orientation = None, so_term=['https://identifiers.org/SO:0000167'],
                         name='Promoter 1', start_seq_range=1, end_seq_range= None)

    assert part_1.part_di() == {"part_type":"Promoter","orientation": None,
                                "so_term": ['https://identifiers.org/SO:0000167'], 
                                "name":'Promoter 1', "start_point":(0,0), "start_seq_range":1, "end_seq_range":None}
