'''
test case for interaction class functions
'''

import dnaplotlib2 as dpl

def test_interaction():
    '''
    function to test added new element to interaction
    '''
    inter_1 = dpl.Interaction('control', 'RBS', 'CDS', 'First Interaction')
    assert inter_1.interaction_append() == {'interaction_type': 'control', 'start_object': 'RBS', 'end_object': 'CDS', 'name': 'First Interaction'}