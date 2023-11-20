from settings import *


def getTableAttrs(table_name):
    table_attrs = []
    if table_name == BookTableName_:
        table_attrs = BookAttrs_
    elif table_name == ReaderTableName_:
        table_attrs = ReaderAttrs_
    elif table_name == BorrowingTableName_:
        table_attrs = BorrowingAttrs_
    return table_attrs


def getTableAttrsRu(table_name):
    table_attrs_ru = []
    if table_name == BookTableName_:
        table_attrs_ru = BookAttrsRu_
    elif table_name == ReaderTableName_:
        table_attrs_ru = ReaderAttrsRu_
    elif table_name == BorrowingTableName_:
        table_attrs_ru = BorrowingAttrsRu_
    return table_attrs_ru


def get_key(dic, value):
    for k, v in dic.items():
        if v == value:
            return k
