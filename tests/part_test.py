import dnaplotlib2 as dpl

def test_part_list():
    
    part_1 = dpl.Part('o',1, "SO:1", 'm')
    assert part_1.part_li() == ['o',1, "SO:1", 'm']
