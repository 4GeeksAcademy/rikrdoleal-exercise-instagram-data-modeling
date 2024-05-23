import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'

    user_from_id = Column(Integer, ForeignKey("User.id"), primary_key = True)
    user_to_id = Column(Integer, ForeignKey("User.id"))

    def serialize(self):
        return{
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    username = Column(String(20), nullable = False, unique = True)
    email = Column(String(20), nullable = False, unique = True)
    password = Column(String(20), nullable = False)
    name = Column(String (20), nullable = False)
    last_name = Column(String (20), nullable = False)

    def serialize (self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "favorites": self.favorites
        }
    
class Comment(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key = True)
    comment_text = Column(String(20), nullable = False)
    authord_id = Column(Integer, ForeignKey("User.id"), nullable = False)
    post_id = Column(Integer, ForeignKey("Post.id"), nullable = False)

    def serialize(self):
        return{
            "id": self.id,
            "comment_text": self.comment_text,
            "authord_id": self.authord_id,
            "post_id": self.post_id
        }
    
class Post(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable = False)

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id
        }

class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key = True)
    type = Column(Enum("MediaType"), nullable = False)
    url = Column(String(50), nullable = False)
    post_id = Column(Integer, ForeignKey("Post.id"), nullable = False)

    def serialize(self):
        return{
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
