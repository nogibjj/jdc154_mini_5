from mylib.transform_load import load


def test_load():
    database = load()
    assert database == "nflReceivers.db"


if __name__ == "__main__":
    test_load()
