from src.aware_dict import AwareDict


def test_aware_dict(capfd):
    dict_ = AwareDict({"a": 1, "b": {"c": 2}})
    dict_["b"]["c"] = 3
    dict_["b"]["d"] = 4
    dict_["e"] = {"f": 5, "g": 6}

    out, _ = capfd.readouterr()
    out = out.split("\n")

    assert out[0] == r"{'a': 1, 'b': {'c': 3}}"
    assert out[1] == r"{'a': 1, 'b': {'c': 3, 'd': 4}}"
    assert out[2] == r"{'a': 1, 'b': {'c': 3, 'd': 4}, 'e': {'f': 5, 'g': 6}}"
