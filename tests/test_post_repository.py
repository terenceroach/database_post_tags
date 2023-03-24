from lib.post_repository import PostRepository
from lib.post import Post
"""
When I call #all on PostRepository
It return all the post in a list
"""
def test_all(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]

"""
When I call find #find on the PostRepository with an id
I get the corresponding post to that id back 
"""
def test_find(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    result = repository.find(3)
    assert result == Post(3, 'Using a REPL')

"""
When I call #create on PostRepository with some fields
And then I call #all
The new post os returned in the list
"""
def test_create(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    post = Post(None, "An added post")
    repository.create(post)
    result = repository.all()
    assert result == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics'),
        Post(8, 'An added post')
    ]

"""
When I call #find_by_tag on PostRepository with a tag_id
A list of posts is returned corresponding to the tag_id
"""
def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)
    result = repository.find_by_tag("travel")
    assert result == [
        Post(4, 'My weekend in Edinburgh'),
        Post(6, 'A foodie week in Spain')
    ]

# """
# When I call #delete on PostRepository with an id
# And then I call #all
# The delete post does not show up
# """
# def test_delete(db_connection):
#     db_connection.seed("seeds/blog_posts_tags.sql")
#     repository = PostRepository(db_connection)
#     repository.delete(4)
#     result = repository.all()
#     assert result == [
#         Post(1, 'How to use Git'),
#         Post(2, 'Fun classes'),
#         Post(3, 'Using a REPL'),
#         Post(5, 'The best chocolate cake EVER'),
#         Post(6, 'A foodie week in Spain'),
#         Post(7, 'SQL basics')
#     ]