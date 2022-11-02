'''
test case for part class functions
'''
import dnaplotlib2 as dpl

def test_part_list():
    '''
    function to test the return of part list function
    '''
    part_1 = dpl.Part(part_type="Promoter", orientation = None, so_term=['https://identifiers.org/SO:0000167'], name='Promoter 1', start_range=1, end_range= None)

    assert part_1.part_li() == ["Promoter", None, ['https://identifiers.org/SO:0000167'], 'Promoter 1', 1, None]
