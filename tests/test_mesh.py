from nimbus.mesh import materialise


def test_region():
    assert materialise('NA-18', 10)['region'] == 'NA-18'
