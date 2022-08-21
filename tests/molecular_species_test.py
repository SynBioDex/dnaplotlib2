import dnaplotlib2 as dpl

def test_moleculer():

    mo_1 = dpl.MolecularSpecies('small moleculer', 'SO:1111', 'First Moleculer')
    assert mo_1.molec_spec_append() == {'molecular_species_type': 'small moleculer', 'so_term': 'SO:1111', 'name': 'First Moleculer'}