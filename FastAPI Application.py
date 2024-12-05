from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database Configuration
DATABASE_URL = "sqlite:///./event_nest.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    events = relationship("Event", back_populates="organizer")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    location = Column(String)
    max_participants = Column(Integer)
    organizer_id = Column(Integer, ForeignKey("users.id"))
    organizer = relationship("User", back_populates="events")

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes

# User Routes
@app.post("/users/")
def create_user(username: str, email: str, password: str, db: SessionLocal = Depends(get_db)):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str = None, email: str = None, password: str = None, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if username: user.username = username
    if email: user.email = email
    if password: user.password = password
    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# Event Routes
@app.post("/events/")
def create_event(title: str, description: str, location: str, max_participants: int, organizer_id: int, db: SessionLocal = Depends(get_db)):
    organizer = db.query(User).filter(User.id == organizer_id).first()
    if not organizer:
        raise HTTPException(status_code=404, detail="Organizer not found")
    event = Event(title=title, description=description, location=location, max_participants=max_participants, organizer_id=organizer_id)
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"message": "Event created successfully", "event": event}

@app.get("/events/")
def get_events(db: SessionLocal = Depends(get_db)):
    events = db.query(Event).all()
    return events

@app.get("/events/{event_id}")
def get_event(event_id: int, db: SessionLocal = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.put("/events/{event_id}")
def update_event(event_id: int, title: str = None, description: str = None, location: str = None, max_participants: int = None, db: SessionLocal = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    if title: event.title = title
    if description: event.description = description
    if location: event.location = location
    if max_participants: event.max_participants = max_participants
    db.commit()
    db.refresh(event)
    return {"message": "Event updated successfully", "event": event}

@app.delete("/events/{event_id}")
def delete_event(event_id: int, db: SessionLocal = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    return {"message": "Event deleted successfully"}
