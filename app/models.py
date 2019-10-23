from . import db
class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.string(255))
    email = db.Column()
    pass_secure = db.Column(db.String(255))
        @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    


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

class PitchCategory(db.model):
    __tablename__ = 'pitchcategory'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    description =db.Column(db.String(255))

