from hello import say_hello


def test_say_hello_returns_hello_world():
    assert say_hello() == "Hello, world!"
