import sbol3

# Define a constant that is not defined in pySBOL3
SO_ENGINEERED_REGION = sbol3.SO_NS + '0000804'
SO_ASSEMBLY_SCAR = sbol3.SO_NS + '0001953'

# Set the default namespace for new objects and create a document
sbol3.set_namespace('https://synbiohub.org/public/igem/')
doc = sbol3.Document()

print('Creating GFP expression cassette')
i13504 = sbol3.Component('I13504', sbol3.SBO_DNA,
                         name='iGEM 2016 interlab reporter',
                         description='GFP expression cassette used for 2016 iGEM interlab',
                         roles=[SO_ENGINEERED_REGION])

# Add the GFP expression cassette to the document
doc.add(i13504)
print(f'Created GFP expression cassette {i13504.identity}')

# Add the Promoter subcomponent
promotor = sbol3.Component('Promotor', sbol3.SBO_DNA)
promotor.name = 'Promotor (Omar)'
promotor.roles.append(sbol3.SO_PROMOTER)
doc.add(promotor)
i13504.features.append(sbol3.SubComponent(promotor))
print(f'Added promotor SubComponent {promotor.identity}')

# Add the RBS subcomponent
rbs = sbol3.Component('RBS', sbol3.SBO_DNA)
rbs.name = 'RBS (Omar)'
rbs.roles.append(sbol3.SO_RBS)
doc.add(rbs)
promotor.features.append(sbol3.SubComponent(rbs))
print(f'Added RBS SubComponent {rbs.identity}')

# Add the GFP subcomponent
gfp = sbol3.Component('GFP', sbol3.SBO_DNA)
gfp.name = 'GFP (Omar)'
gfp.roles.append(sbol3.SO_CDS)
doc.add(gfp)
rbs.features.append(sbol3.SubComponent(gfp))
print(f'Added GFP SubComponent {gfp.identity}')

# Add the terminator
term = sbol3.Component('Term', sbol3.SBO_DNA)
term.name = 'double terminator (Omar)'
term.roles.append(sbol3.SO_TERMINATOR)
doc.add(term)
gfp.features.append(sbol3.SubComponent(term))
print(f'Added Terminator SubComponent {term.identity}')


# --------------------------------------------------
# Finally, write the data out to a file
# --------------------------------------------------
doc.write('dfs_linner_case.nt', sbol3.SORTED_NTRIPLES)
