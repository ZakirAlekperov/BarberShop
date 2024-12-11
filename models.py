from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Client(db.Model):
    client_id=db.Column(db.Integer, primary_key=True)
    client_name=db.Column(db.String(100),nullable=False)
    client_phone_number=db.Column(db.String(20),nullable=False)
    client_email=db.Column(db.String(100),nullable=False)
    is_permonent_client=db.Column(db.Bullian,default=False)

    def __repr__(self):
        return f"id: {self.client_id}, name: {self.client_name}, phone number: {self.client_phone_number}, email: {self.client_email}, permonent: {self.is_permonent_client}"
    
    
class User(db.Model):
    
    
    def __repr__(self):
        pass
    

class Service(db.Model):
    
    def __repr__(self):