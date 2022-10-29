import sbol3
'''
This file creates a .nt sbol file which contains two backbones and molecule to draw
'''

# Define a constant that is not defined in pySBOL3
SO_ENGINEERED_REGION = sbol3.SO_NS + '0000804'
SO_ASSEMBLY_SCAR = sbol3.SO_NS + '0001953'

# Set the default namespace for new objects and create a document
sbol3.set_namespace('https://synbiohub.org/public/igem/')
doc = sbol3.Document()

### First Backbone
print('Creating GFP expression cassette')
i13504 = sbol3.Component('I13504', sbol3.SBO_DNA,
                         name='iGEM 2016 interlab reporter',
                         description='GFP expression cassette used for 2016 iGEM interlab',
                         roles=[SO_ENGINEERED_REGION])

# Add the GFP expression cassette to the document
doc.add(i13504)
print(f'Created GFP expression cassette {i13504.identity}')

# Add the Promoter subcomponent
promotor1 = sbol3.Component('Promotor1', sbol3.SBO_DNA)
promotor1.name = 'Promotor (Omar)'
promotor1.roles.append(sbol3.SO_PROMOTER)
doc.add(promotor1)
i13504.features.append(sbol3.SubComponent(promotor1))
print(f'Added promotor1 SubComponent {promotor1.identity}')

# Add the RBS subcomponent
rbs1 = sbol3.Component('RBS1', sbol3.SBO_DNA)
rbs1.name = 'RBS (Omar)'
rbs1.roles.append(sbol3.SO_RBS)
doc.add(rbs1)
i13504.features.append(sbol3.SubComponent(rbs1))
print(f'Added RBS SubComponent {rbs1.identity}')

# Add the GFP subcomponent
gfp1 = sbol3.Component('GFP1', sbol3.SBO_DNA)
gfp1.name = 'GFP (Omar)'
gfp1.roles.append(sbol3.SO_CDS)
doc.add(gfp1)
i13504.features.append(sbol3.SubComponent(gfp1))
print(f'Added GFP SubComponent {gfp1.identity}')

# Add the terminator
term1 = sbol3.Component('Term1', sbol3.SBO_DNA)
term1.name = 'double terminator (Omar)'
term1.roles.append(sbol3.SO_TERMINATOR)
doc.add(term1)
i13504.features.append(sbol3.SubComponent(term1))
print(f'Added Terminator SubComponent {term1.identity}')

#-----------------------------------------------------------------


### Second Backbone

sec_back = sbol3.Component('sec_back', sbol3.SBO_DNA,
                         name='iGEM 2016 interlab reporter',
                         description='GFP expression cassette used for 2016 iGEM interlab',
                         roles=[SO_ENGINEERED_REGION])

# Add the GFP expression cassette to the document
doc.add(sec_back)
print(f'Created GFP expression cassette {sec_back.identity}')

# Add the Promoter subcomponent
promotor2 = sbol3.Component('Promotor2', sbol3.SBO_DNA)
promotor2.name = 'Promotor (Omar2)'
promotor2.roles.append(sbol3.SO_PROMOTER)
doc.add(promotor2)
sec_back.features.append(sbol3.SubComponent(promotor2))
print(f'Added promotor SubComponent {promotor2.identity}')

# Add the Operator subcomponent
op1 = sbol3.Component('op1', sbol3.SBO_DNA)
op1.name = 'Operator (Omar2)'
op1.roles.append(sbol3.SO_OPERATOR)
doc.add(op1)
sec_back.features.append(sbol3.SubComponent(op1))
print(f'Added operator SubComponent {op1.identity}')

# Add the RBS subcomponent
rbs2 = sbol3.Component('RBS2', sbol3.SBO_DNA)
rbs2.name = 'RBS (Omar2)'
rbs2.roles.append(sbol3.SO_RBS)
doc.add(rbs2)
sec_back.features.append(sbol3.SubComponent(rbs2))
print(f'Added RBS SubComponent {rbs2.identity}')

# Add the GFP subcomponent
gfp2 = sbol3.Component('GFP2', sbol3.SBO_DNA)
gfp2.name = 'GFP (Omar2)'
gfp2.roles.append(sbol3.SO_CDS)
doc.add(gfp2)
sec_back.features.append(sbol3.SubComponent(gfp2))
print(f'Added GFP SubComponent {gfp2.identity}')

# Add the terminator
term2 = sbol3.Component('Term2', sbol3.SBO_DNA)
term2.name = 'double terminator (Omar2)'
term2.roles.append(sbol3.SO_TERMINATOR)
doc.add(term2)
sec_back.features.append(sbol3.SubComponent(term2))
print(f'Added Terminator SubComponent {term2.identity}')

#-----------------------------------------------------------------


### Adding sequance range to components
seq_13504 = ('aaagaggagaaatactagatgcgtaaaggagaagaacttttcactggagttgtcccaattcttgttgaat'
             'tagatggtgatgttaatgggcacaaattttctgtcagtggagagggtgaaggtgatgcaacatacggaaa'
             'acttacccttaaatttatttgcactactggaaaactacctgttccatggccaacacttgtcactactttc'
             'ggttatggtgttcaatgctttgcgagatacccagatcatatgaaacagcatgactttttcaagagtgcca'
             'tgcccgaaggttatgtacaggaaagaactatatttttcaaagatgacgggaactacaagacacgtgctga'
             'agtcaagtttgaaggtgatacccttgttaatagaatcgagttaaaaggtattgattttaaagaagatgga'
             'aacattcttggacacaaattggaatacaactataactcacacaatgtatacatcatggcagacaaacaaa'
             'agaatggaatcaaagttaacttcaaaattagacacaacattgaagatggaagcgttcaactagcagacca'
             'ttatcaacaaaatactccaattggcgatggccctgtccttttaccagacaaccattacctgtccacacaa'
             'tctgccctttcgaaagatcccaacgaaaagagagaccacatggtccttcttgagtttgtaacagctgctg'
             'ggattacacatggcatggatgaactatacaaataataatactagagccaggcatcaaataaaacgaaagg')

i13504_seq = sbol3.Sequence('I13504_sequence')
i13504_seq.elements = seq_13504
i13504_seq.encoding = sbol3.IUPAC_DNA_ENCODING
i13504.sequences.append(i13504_seq)


loc = sbol3.Range(i13504_seq, 0, 70)
i13504_seq_feat = sbol3.SequenceFeature([loc])
i13504_seq_feat.roles = [SO_ASSEMBLY_SCAR]
i13504.features.append(i13504_seq_feat)



### Add Molecule to the document
mol_sp = sbol3.Component('Molecule', sbol3.SBO_RNA)
mol_sp.name = 'Single Strand Nucleic Acid (Omar)'
mol_sp.roles.append(sbol3.SBO_RNA)
doc.add(mol_sp)
print(f'Added Terminator SubComponent {mol_sp.identity}')

# --------------------------------------------------
# Finally, write the data out to a file
# --------------------------------------------------
doc.write('two_backbones_and_molecule_case.nt', sbol3.SORTED_NTRIPLES)
