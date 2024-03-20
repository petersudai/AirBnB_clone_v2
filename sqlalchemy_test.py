from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine
engine = create_engine('sqlite:///:memory:', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a simple User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some users
session.add_all([
    User(name='Alice', age=30),
    User(name='Bob', age=35),
    User(name='Charlie', age=25)
])

# Commit the session to persist changes
session.commit()

# Query the database
users = session.query(User).all()
print("All users:")
for user in users:
    print(user)

# Close the session
session.close()
