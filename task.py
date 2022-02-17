import pytest


def is_caps_on(string):  #str, которая будет тестироваться тестами ниже
    if string.isupper():
        return True
    elif string == 'vk':
        return 'Bingo!'
    else:
        return False


def test_str1():
    assert is_caps_on('STRING')
    assert not is_caps_on('STRINg')
    assert is_caps_on('vk') == 'Bingo!'


def test_str2():
    try:
        assert is_caps_on(1702)
    except AttributeError:
        pass
        

@pytest.mark.parametrize('test_input,expected', [('STRING', True), ('STRINg', False), ('vk', 'Bingo!')])
def test_str3(test_input, expected):
    assert is_caps_on(test_input) == expected
    

def int_converter(integer):  #int функция, которая будет тестироваться тестами ниже
    if type(integer) == int:
        return integer
    elif type(integer) == float:
        return int(integer)
    elif type(integer) == str:
        return int(integer)


def test_int1():
    assert int_converter(17.1) == 17
    assert int_converter(17) == 17
    assert int_converter('17') == 17


def test_int2():
    try:
        assert int_converter('VK')
    except ValueError:
        pass
        

@pytest.mark.parametrize('test_input,expected', [(17, 17), (17.1, 17), ('17', 17)])
def test_int3(test_input, expected):
    assert int_converter(test_input) == expected
