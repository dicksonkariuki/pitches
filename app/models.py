from . import db
class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.string(255))

    def __repr__(self):
        return f'User {self.username}'
class Comment(db.model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    user_id =db.Column(db.Integer,db.ForeignKey("users.id"))
    comment_id = db.Column(db.Integer(255))
     

class Pitches(db.model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

