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
        return "<Group: {}>".format(self.name

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
    group_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    donated = db.Column(db.Float, nullable = False)

    def __init__(self, name):
        self.name = name

    def get_group_members(id):
        return Group.query.filter_by(group_id=id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Group: {}>".format(self.name)
