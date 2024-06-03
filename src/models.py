from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_favorite_planets = db.Table('user_favorite_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True)
)

user_favorite_vehicles = db.Table('user_favorite_vehicles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)
)

user_favorite_persons = db.Table('user_favorite_persons',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('person_id', db.Integer, db.ForeignKey('persons.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_planets = db.relationship('Planet', secondary=user_favorite_planets, backref=db.backref('users', lazy=True))
    favorite_vehicles = db.relationship('Vehicle', secondary=user_favorite_vehicles, backref=db.backref('users', lazy=True))
    favorite_persons = db.relationship('Person', secondary=user_favorite_persons, backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    population = db.Column(db.BigInteger, nullable=False)
    climate = db.Column(db.String(64), nullable=False)
    terrain = db.Column(db.String(64), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain
            }
    
class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    dimensions = db.Column(db.String(32), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'dimensions': self.dimensions,
            }

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'age': self.age
            }
