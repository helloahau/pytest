from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("SZ", 100.1, 200.2)
    assert (100.1, 200.2) == p1.get_lat_long()
