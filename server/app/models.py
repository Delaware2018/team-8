from app import db

class Group(db.Model):

    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    donated = db.Column(db.Float)
    userids = db.relationship("User", lazy=True)




##USER TABLE
class User(db.Model):

    __tablename__ = 'Users'

    #name
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))

    #address
    line_1 = db.Column(db.String(100))
    line_2 = db.Column(db.String(100))
    city = db.Column(db.String(50))
    zipcode = db.Column(db.Integer)
    country = db.Column(db.String(50))


    phone_number = db.Column(db.String(10))
    date_joined = db.Column(db.DateTime, default=db.func.current_timestamp())

    #personal
    personal_donations = db.Column(db.Integer)
    income = db.Column(db.Integer)
    bio = db.Column(db.String(256))
    # profile_pic = db.Column()



    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_all():
        return Group.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Group: {}>".format(self.name)
