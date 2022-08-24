'''
test case for interaction node class functions
'''
import dnaplotlib2 as dpl

def test_interaction_node():
    '''
    function to test append function of interaction node
    '''
    
    node_1 = dpl.InteractionNode('direct', 'SO:5555', 'First InteractionNode')
    assert node_1.node_dict() == {'interaction_node_type' : 'direct', 'so_term': 'SO:5555', 'name' : 'First InteractionNode'}