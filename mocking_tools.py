import pytest

class MyClass:
    pass

my_obj = MyClass()

def test_pretend(mocker):

    # 1 - Mock a function that is called within the code being tested
    mocker.patch('path.to.code.being.tested.func_being_mocked')

    # 2 - Mock a method on an object which is passed to the code being tested
    mocker.patch.object(my_obj, 'my_method')

    # 3 - Mock a method on a class which is instantiated within the code being tested
    mocker.patch.object(MyClass, 'my_method')

    # 4 - Use a mock object as input to a class or function since the actual input is “complicated”
    mocker.MagicMock(some_attr='my mock needs this attr')

    # ^^^ can pass return_value or side_effect to any of the above

    # 5 - Mock environment variables
    mocker.patch.dict('path.to.code.being.tested.os.environ', {'MOCK': 'ENVVAR'}, clear=True)
