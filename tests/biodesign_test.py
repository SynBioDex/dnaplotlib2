'''
test case to for biodesign 
'''

import dnaplotlib2 as dpl

def test_biodesign():
    '''
    funtion to test return of biodesign and make sure every element have been added
    '''

    bio_1 =  dpl.BioDesign('First BioDesign')
    bio_1.add_backbone('Backbone1')
    bio_1.add_moleculer('Moleculer1')
    bio_1.add_interaction_node('Node1')
    bio_1.add_interaction('Interaction')
    bio_1.show_biodesign()

    assert bio_1.biodesign_output == ['First BioDesign',['Backbone1'], ['Moleculer1'],['Node1'],['Interaction']]