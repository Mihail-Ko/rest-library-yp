
def getColumnSize(attr_name):
    attr_line_size = 200
    if attr_name == 'id':
        attr_line_size = 40
    elif attr_name == 'year':
        attr_line_size = 40
    elif attr_name == 'bookId':
        attr_line_size = 40
    elif attr_name == 'readerId':
        attr_line_size = 40
    elif attr_name == 'borrowingDate':
        attr_line_size = 70
    elif attr_name == 'limitDate':
        attr_line_size = 70
    elif attr_name == 'returned':
        attr_line_size = 50
    return attr_line_size
