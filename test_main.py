from mylib.transform_load import load


def test_load():
    l = load()
    assert l == "nflReceivers.db"


if __name__ == "__main__":
    test_load()
