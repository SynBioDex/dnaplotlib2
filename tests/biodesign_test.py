'''
test case for biodesign 
'''

import dnaplotlib2 as dpl

def test_biodesign_add_backbone
():
    '''
    funtion to test return of biodesign and make sure every element have been added
    '''

    part_1 = dpl.Part(
        part_type="Promoter",
        orientation=None,
        so_term=["https://identifiers.org/SO:0000167"],
        name="Promoter 1",
        start_seq_range=1,
        end_seq_range=None,
    )

    part_2 = dpl.Part(
        part_type="Promoter",
        orientation=None,
        so_term=["https://identifiers.org/SO:0000167"],
        name="Promoter 2",
        start_seq_range=5,
        end_seq_range=None,
    )

    backbone1 = dpl.Backbone(name="backbone 1")
    backbone1.append_part(part_1.part_di())
    backbone1.append_part(part_2.part_di())


    part_3 = dpl.Part(
        part_type="Promoter",
        orientation=None,
        so_term=["https://identifiers.org/SO:0000167"],
        name="Promoter 3",
        start_seq_range=10,
        end_seq_range=None,
    )

    part_4 = dpl.Part(
        part_type="Promoter",
        orientation=None,
        so_term=["https://identifiers.org/SO:0000167"],
        name="Promoter 4",
        start_seq_range= 15,
        end_seq_range=None,
    )
    backbone2 = dpl.Backbone(name="backbone 2")
    backbone2.append_part(part_3.part_di())
    backbone2.append_part(part_4.part_di())

    bio_1 =  dpl.BioDesign('First BioDesign')
    bio_1.add_backbone(backbone1)
    bio_1.add_backbone(backbone2)
    

    output = [[
        {
            "part_type": "Promoter",
            "orientation": None,
            "so_term": ["https://identifiers.org/SO:0000167"],
            "name": "Promoter 1",
            "start_point": (0, 0),
            "start_seq_range": 1,
            "end_seq_range": None,
        },
        {
            "part_type": "Promoter",
            "orientation": None,
            "so_term": ["https://identifiers.org/SO:0000167"],
            "name": "Promoter 2",
            "start_point": (0, 0),
            "start_seq_range": 5,
            "end_seq_range": None,
        }],
        [{
            "part_type": "Promoter",
            "orientation": None,
            "so_term": ["https://identifiers.org/SO:0000167"],
            "name": "Promoter 3",
            "start_point": (0, 0),
            "start_seq_range": 10,
            "end_seq_range": None,
        },
        {
            "part_type": "Promoter",
            "orientation": None,
            "so_term": ["https://identifiers.org/SO:0000167"],
            "name": "Promoter 4",
            "start_seq_range": 15,
            "start_point": (0, 0),
            "end_seq_range": None,
        }]
    ]

    output_backbones_size = 0
    correct_tests = 0
    for back_list, out_list in zip(bio_1.backbones, output):
        output_backbones_size += len(out_list)
        for part_dict, out_dict in zip(back_list.backbones, out_list):
            for key in part_dict:
                if part_dict[key] == out_dict[key]:
                    correct_tests += 1

    assert correct_tests == output_backbones_size * len(output[0][0])