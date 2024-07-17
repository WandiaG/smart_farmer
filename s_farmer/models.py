import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

from s_farmer import db


Base = declarative_base()


class CustomerDefault(db.Model, Base):
    __tablename__ = 'customer_default'
    id = Column(Integer, primary_key=True)  # Add this line
    mno = Column(Integer)
    price = Column(Float)

class Advance(db.Model, Base):
    __tablename__ = 'advance'
    id = Column(Integer, primary_key=True)
    pvno = db.Column(db.Integer)
    mno = db.Column(db.Integer)
    amount = db.Column(db.Float)
    name = db.Column(db.Text)

class Store(db.Model, Base):
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    mno = Column(Integer)
    price = Column(Float)

class Ai(db.Model, Base):
    __tablename__ = 'ai'
    id = Column(Integer, primary_key=True)
    mno = Column(Integer)
    price = Column(Float)

class DEF(db.Model, Base):
    __tablename__ = 'DEF'
    id = Column(Integer, primary_key=True)
    mno = Column(Integer)
    price = Column(Float)

class Jamaa(db.Model, Base):
    __tablename__ = 'jamaa'
    id = Column(Integer, primary_key=True)
    mno = Column(Integer)
    price = Column(Float)

class SpDefault(db.Model, Base):
    __tablename__ = 'sp_default'
    id = Column(Integer, primary_key=True)
    mno = Column(Integer)
    price = Column(Float)

class Customer(db.Model, Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    member_code = db.Column(db.Integer, primary_key=True)
    member_bank_acct = db.Column(db.Text)
    member_name = db.Column(db.Text)
    meber_kgs = db.Column(db.Float)
    route_code = db.Column(db.Integer)
    route_name = db.Column(db.Text)
    member_id_num = db.Column(db.Text)
    route = db.Column(db.Text)


# ... other models for other tables

def load_data_from_excel(sheet_name, table_name):
    data_file = "farmers.xlsx"
    df = pd.read_excel(data_file, sheet_name=sheet_name)

    engine = create_engine('sqlite:///menuinfor.db')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        session.commit()
    except Exception as e:
        print(f"Error loading data for {sheet_name}: {e}")
        session.rollback()
    finally:
        session.close()

# Call the function for each sheet
load_data_from_excel("customer_default", "customer_default")
load_data_from_excel("ai", "ai")
load_data_from_excel("store", "store")
load_data_from_excel("advance", "advance")
load_data_from_excel("sp_default", "sp_default")
load_data_from_excel("DEF", "DEF")
load_data_from_excel("jamaa", "jamaa")
load_data_from_excel("farmers", "customers")
