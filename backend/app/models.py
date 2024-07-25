from .database import Base
from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(50), unique=True, index=True)
    parent_department_id = Column(Integer, ForeignKey('departments.department_id'))
    start_date = Column(Integer)
    end_date = Column(Integer, nullable=True)
    parent = relationship("Department", remote_side=[department_id])
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    role = Column(Integer)
    primary_department_id = Column(Integer, ForeignKey('departments.department_id'))
    primary_position = Column(String(100))
    start_date = Column(Integer)
    end_date = Column(Integer, nullable=True)
    department = relationship("Department")
    
class UserPosition(Base):
    __tablename__ = 'user_positions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    position = Column(String(100))
    kenmu = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer, nullable=True)
    user = relationship("User")
    department = relationship("Department")
    
class ChangeHistory(Base):
    __tablename__ = 'change_histories'
    change_id = Column(Integer, primary_key=True, index=True)
    entity = Column(String(100))
    entity_id = Column(Integer)
    change_type = Column(String(100))
    changed_by = Column(Integer, ForeignKey('users.id'))
    change_date = Column(Integer)
    old_value = Column(String(100), nullable=True)
    new_value = Column(String(100), nullable=True)
    user = relationship("User")