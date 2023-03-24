from lib.post import Post
"""
A post instance has properties id and title
"""
def test_post_properties():
    post = Post(1, "The first title")
    assert post.id == 1
    assert post.title == "The first title"

"""
2 instances that are the same return as being equal
"""
def test_equality():
    post_1 = Post(1, "The first title")
    post_2 = Post(1, "The first title")
    assert post_1 == post_2

"""
A nicely foirmatted string is returned
"""
def test_formatting():
    post = Post(1, "The first title")
    assert str(post) == "Post(1, The first title)"
