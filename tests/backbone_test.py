"""
test case for backbone class functions
"""

import dnaplotlib2 as dpl


def test_backbone_append():
    """
    functiont to test return function of backbone class
    """
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

    backbone1 = dpl.Backbone(name="test1")
    backbone1.append_part(part_1.part_di())
    backbone1.append_part(part_2.part_di())
    backbone1.append_part(part_3.part_di())
    backbone1.append_part(part_4.part_di())

    output = [
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
        },
        {
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
        },
    ]


    correct_tests = 0
    # iterate over backbone parts and output parts 
    for b_dict, out_dict in zip(backbone1.backbones, output):
        # iterate over parts in backbone and use same dictionary key to compare values with output dictionary
        for key in b_dict:
            if b_dict[key] == out_dict[key]:
                correct_tests += 1

    assert correct_tests == len(backbone1.backbones) * len(backbone1.backbones[0])
