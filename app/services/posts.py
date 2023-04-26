from app.models.post import Post

def getAllPosts():
    return [post.serialize() for post in Post.query.all()]