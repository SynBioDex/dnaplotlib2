'''
test case for part class functions
'''
import dnaplotlib2 as dpl

def test_part_list():
    '''
    function to test the return of part list function
    '''
    part_1 = dpl.Part('o',1, "SO:1", 'm')
    assert part_1.part_li() == ['o',1, "SO:1", 'm',(0, 0)]
