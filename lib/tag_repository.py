from lib.tag import Tag
class TagRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM tags")
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)
        return tags
    
    def find(self, tag_id):
        rows = self._connection.execute("SELECT * FROM tags WHERE id = %s", [tag_id])
        row = rows[0]
        return Tag(row['id'], row['name'])
    
    def create(self, tag):
        self._connection.execute("INSERT INTO tags (name) VALUES (%s)", [tag.name])

    def find_by_post(self, post_id):
        rows = self._connection.execute("SELECT tags.id, tags.name FROM tags JOIN posts_tags ON posts_tags.tag_id = tags.id JOIN posts ON posts_tags.post_id = posts.id WHERE posts.id = 2")
        tags = []
        for row in rows:
            tag = Tag(row['id'], row['name'])
            tags.append(tag)
        return tags
