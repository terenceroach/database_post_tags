from lib.tag import Tag
"""
A tag instance has properties id and name
"""
def test_tag_properties():
    tag = Tag(1, "How to use Git")
    assert tag.id == 1
    assert tag.name == "How to use Git"

"""
2 instances that are the same return as being equal
"""
def test_equality():
    tag_1 = Tag(1, "How to use Git")
    tag_2 = Tag(1, "How to use Git")
    assert tag_1 == tag_2

"""
A nicely foirmatted string is returned
"""
def test_formatting():
    tag = Tag(1, "How to use Git")
    assert str(tag) == "Tag(1, How to use Git)"