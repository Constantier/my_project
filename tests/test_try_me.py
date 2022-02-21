from my_project.lib import try_me

def test_type():
    assert(type(try_me() is str))

def test_content():
    assert(try_me()=='Hello World')
