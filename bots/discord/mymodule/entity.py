# coding: utf-8
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()

Object = Table(
    'objects', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(32), nullable=False),
)
