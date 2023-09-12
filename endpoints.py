from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from .models import ContactCreate, ContactUpdate, Contact
from .database import get_db
from datetime import date, timedelta

app = FastAPI()

@app.post("/contacts/", response_model=ContactCreate)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.get("/contacts/", response_model=list[ContactCreate])
def get_all_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@app.get("/contacts/{contact_id}", response_model=ContactCreate)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@app.put("/contacts/{contact_id}", response_model=ContactCreate)
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.delete("/contacts/{contact_id}", response_model=ContactCreate)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(db_contact)
    db.commit()
    return db_contact

@app.get("/search/")
def search_contacts(
    q: str = Query(None, title="Search query", min_length=1, max_length=50),
    db: Session = Depends(get_db)
):
    contacts = db.query(Contact).filter(
        (Contact.first_name.ilike(f"%{q}%"))
        | (Contact.last_name.ilike(f"%{q}%"))
        | (Contact.email.ilike(f"%{q}%"))
    ).all()
    return contacts

@app.get("/upcoming_birthdays/", response_model=list[ContactCreate])
def get_upcoming_birthdays(db: Session = Depends(get_db)):
    today = date.today()
    next_week = today + timedelta(days=7)
    contacts = db.query(Contact).filter(
        (Contact.birthday >= today) & (Contact.birthday <= next_week)
    ).all()
    return contacts
