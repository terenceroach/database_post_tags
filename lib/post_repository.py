from lib.post import Post
class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"])
            posts.append(post)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row["title"])
    
    def create(self, post):
        self._connection.execute("INSERT INTO posts (title) VALUEs (%s)", [post.title])

    # def delete(self, post_id):
    #     self._connection.execute("DELETE FROM posts WHERE id = %s", [post_id])

    def find_by_tag(self, tag):
        rows = self._connection.execute("SELECT posts.id, posts.title FROM posts JOIN posts_tags ON posts_tags.post_id = posts.id JOIN tags ON posts_tags.tag_id = tags.id WHERE tags.name = 'travel'")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"])
            posts.append(post)
        return posts
