from lib.tag_repository import TagRepository
from lib.tag import Tag
"""
When I call #all on TagRepository
It return all the tag in a list
"""
def test_all(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    result = repository.all()
    assert result == [
        Tag(1, 'coding'),
        Tag(2, 'travel'),
        Tag(3, 'cooking'),
        Tag(4, 'education')
    ]


"""
When I call find #find on the TagRepository with an id
I get the corresponding tag to that id back 
"""
def test_find(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    result = repository.find(3)
    assert result == Tag(3, 'cooking')

    """
When I call #create on TagRepository with some fields
And then I call #all
The new tag is returned in the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    tag = Tag(None, "An added tag")
    repository.create(tag)
    result = repository.all()
    assert result == [
        Tag(1, 'coding'),
        Tag(2, 'travel'),
        Tag(3, 'cooking'),
        Tag(4, 'education'),
        Tag(5, 'An added tag')
    ]

"""
When I call #find_by_post on TagRepository with a post_id
A list of tags is returned corresponding to the post_id
"""
def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)
    result = repository.find_by_post(2)
    assert result == [
        Tag(1, 'coding'),
        Tag(4, 'education')
    ]