'''
test case for molecular species class functions
'''
import dnaplotlib2 as dpl

def test_moleculer():
    '''
    function to test molecular species appending 
    '''
    mo_1 = dpl.MolecularSpecies('small moleculer', 'SO:1111', 'First Moleculer')
    mo_1.molec_spec_append()
    assert mo_1.species == {'molecular_species_type': 'small moleculer', 'so_term': 'SO:1111', 'name': 'First Moleculer'}