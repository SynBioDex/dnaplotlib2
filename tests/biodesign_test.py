import dnaplotlib2 as dpl

def test_biodesign():

    bio_1 =  dpl.BioDesign('First BioDesign')
    bio_1.add_backbone('Backbone1')
    bio_1.add_moleculer('Moleculer1')
    bio_1.add_interaction('Interaction')
    bio_1.add_interaction_node('Node1')

    assert bio_1.return_biodesign() == ['First BioDesign',['Backbone1'], ['Moleculer1'],['Node1'],['Interaction']]