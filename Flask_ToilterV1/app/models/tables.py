from app import db

class User(db.Model):
    __tablename__="users"
    id = db.Colum(db.Integer, primary_key=True)
    username = db.Colum(db.String, unique=True)
    password = db.Colum(db.Sting)
    name = db.Colum(db.String)
    email = db.Colum(db.Sting, unique=True)

    def __int__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Colum(db.Integer, primary_key=True)
    content = db.Colum(db.Text)
    user_id = db.Colum(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __int__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r" % self.id

class Follow(db.Model):
    __table__ = "follow"

    id = db.Colum(db.Integer, primary_key=True)
    user_id = db.Colum(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Colum(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)
    flolower = db.relationship('User', foreign_keys=follower_id)



