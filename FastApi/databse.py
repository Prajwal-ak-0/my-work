from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import URL, create_engine

connection_string = URL.create(
    'postgresql',
    username='rag-gpt_owner',
    password='A3xQJVRj1SEC',
    host='ep-restless-hall-a5vpjlwg.us-east-2.aws.neon.tech',
    database='rag-gpt',
    connect_args={'sslmode':'require'}
)

engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()