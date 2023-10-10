from shop import db, app
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=False, nullable=False) 
    profile: Mapped[str] = mapped_column(String, unique=False, nullable=False, default='profile.jpg')

    def __repf__(self):
        return '<User %r>' % self.username
    
with app.app_context():
    db.create_all()
# i don't know why i need to comment this line but i think it's because i already created the database