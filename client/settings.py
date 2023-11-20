BookTableName_ = 'book'
BookAttrsRu_ = ['Номер', 'Название', 'Автор', 'Год издания']
BookAttrs_ = ['id', 'name', 'author', 'year']

ReaderTableName_ = 'reader'
ReaderAttrsRu_ = ['Номер', 'Имя', 'Фамилия', 'Отчество', 'Телефон']
ReaderAttrs_ = ['id', 'name', 'surname', 'secondName', 'telephone']

BorrowingTableName_ = 'borrowing'
BorrowingAttrsRu_ = ['Номер', '№ книги', '№ читателя', 'Дата выдачи', 'Срок', 'Статус возврата']
BorrowingAttrs_ = ['id', 'bookId', 'readerId', 'borrowingDate', 'limitDate', 'returned']

TableNameRu_ = {
    BookTableName_: 'Книги',
    ReaderTableName_: 'Читатели',
    BorrowingTableName_: 'Выдача'
}

StatisticAttrs_ = ['id', 'name', 'author', 'year', 'borrowing_count']
StatisticAttrsRu_ = ['Номер', 'Название', 'Автор', 'Год издания', 'Выдано раз']

BookBorrowingName_ = 'book_borrowing'
BookBorrowingAttrs_ = ['borrowing_id', 'book_name', 'book_id', 'author', 'returned', 'borrowing_date', 'limit_date',
                       'reader_id', 'reader_name']
BookBorrowingAttrsRu_ = ['Номер выдачи', 'Название книги', 'Номер книги', 'Автор', 'Возвращена', 'Дата выдачи', 'Срок',
                         'Номер читателя', 'Имя']

BookBorrowingEndpoints_ = ['in', 'over', 'all']


API_URL = 'http://127.0.0.2/'


WindowHeight_ = 700
WindowWidthMain_ = 1366
WindowWidthStats_ = 1366  # 700
WindowWidthBB_ = 1366  # 1200
