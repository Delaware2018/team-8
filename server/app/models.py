from app import db

class Group(db.Model):

    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    donated = db.Column(db.Float, nullable = False)

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

class GroupUser(db.Model):

    __tablename__ = 'groupusers'
    id = db.Column(db.Integer, primary_key = True)
    group_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    donated = db.Column(db.Float, nullable = False)

    def __init__(self, group_id):
        self.group_id = group_id

    def get_group_members(id):
        return Group.query.filter_by(group_id=id)

    def get_user_groups(id):
        return Group.query.filter_by(user_id=id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<GroupUser: {}>".format(self.name)

class User(db.Model):

    __tablename__ = 'users'

    #name
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(10000), nullable=False)

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

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def password_is_valid(self, password):
        return Bcrypt().check_password_hash(self.password, password)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)
