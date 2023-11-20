from PyQt6.QtCore import QSize
from PyQt6.QtGui import QCloseEvent

from add_book_form import AddBookForm
from add_reader_form import AddReaderForm
from add_borrowing_form import AddBorrowingForm
from library_client_gui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QLineEdit, QSizePolicy, QLabel
from settings import *
from api import get_page, delete_req, update, search, get_statistic
from api import get_book_borrowing as get_b_b
import util
from ui.gui_setting import getColumnSize


class MainWindow(QMainWindow, Ui_MainWindow):
    # todo crate data class
    login_saved = ''
    password_saved = ''
    xsrf = ''

    book_current_page = 1
    reader_current_page = 1
    borrowing_current_page = 1
    b_b_current_page = 1

    selected_table = None

    current_endp_mode = None

    isStatsTableInit = False
    isBookBorrowTableInit = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.resize(WindowWidthMain_, WindowHeight_)
        self.book_next_button.clicked.connect(lambda: self.nextPage(BookTableName_))
        self.reader_next_button.clicked.connect(lambda: self.nextPage(ReaderTableName_))
        self.borrowing_next_button.clicked.connect(lambda: self.nextPage(BorrowingTableName_))

        self.book_back_button.clicked.connect(lambda: self.backPage(BookTableName_))
        self.reader_back_button.clicked.connect(lambda: self.backPage(ReaderTableName_))
        self.borrowing_back_button.clicked.connect(lambda: self.backPage(BorrowingTableName_))

        self.refresh_books_button.clicked.connect(lambda: self.refreshTableWid(BookTableName_))
        self.refresh_readers_button.clicked.connect(lambda: self.refreshTableWid(ReaderTableName_))
        self.refresh_borrowing_button.clicked.connect(lambda: self.refreshTableWid(BorrowingTableName_))
        self.refresh_all_button.clicked.connect(self.refreshAllTableWid)

        self.books_table.itemSelectionChanged.connect(lambda: self.itemSelection(BookTableName_))
        self.readers_table.itemSelectionChanged.connect(lambda: self.itemSelection(ReaderTableName_))
        self.borrowing_table.itemSelectionChanged.connect(lambda: self.itemSelection(BorrowingTableName_))

        self.delete_button.clicked.connect(self.deleteClick)
        self.save_button.clicked.connect(self.saveClick)

        self.save_button.hide()
        self.delete_button.hide()

        self.addBookForm = AddBookForm(self)
        self.addReaderForm = AddReaderForm(self)
        self.addBorrowingForm = AddBorrowingForm(self)

        self.add_book_button.clicked.connect(lambda: self.addClick(BookTableName_))
        self.add_reader_button.clicked.connect(lambda: self.addClick(ReaderTableName_))
        self.add_borrowing_button.clicked.connect(lambda: self.addClick(BorrowingTableName_))

        self.table_comboBox.addItems([TableNameRu_[BookTableName_], TableNameRu_[ReaderTableName_], TableNameRu_[BorrowingTableName_]])

        self.search_button.clicked.connect(self.searchClick)
        self.clear_search_button.clicked.connect(self.searchReset)

        self.statistic_button.clicked.connect(self.statisticClick)
        self.in_borrowing_button.clicked.connect(lambda: self.bookBorrowingClick('in'))
        self.non_returned_button.clicked.connect(lambda: self.bookBorrowingClick('over'))
        self.all_borrowing_button.clicked.connect(lambda: self.bookBorrowingClick('all'))
        # statistic page
        self.return_button_statistic.clicked.connect(self.returnStatisticClick)
        self.refresh_button_statistic.clicked.connect(self.refreshStatsTableWid)
        # borrowed page
        self.return_button_borrowed.clicked.connect(self.returnBorrowingClick)
        self.next_button_borrowed.clicked.connect(lambda: self.nextPage(BookBorrowingName_))
        self.back_button_borrowed.clicked.connect(lambda: self.backPage(BookBorrowingName_))
        self.refresh_button_borrowed.clicked.connect(lambda: self.refreshBookBorrowTableWid(self.current_endp_mode))

    def initAuthVars(self, login, password, xsrf):
        self.login_saved = login
        self.password_saved = password
        self.xsrf = xsrf

        self.addBookForm.initAuthVars(login, password, xsrf)
        self.addReaderForm.initAuthVars(login, password, xsrf)
        self.addBorrowingForm.initAuthVars(login, password, xsrf)

    def reformatTablesGui(self):
        self.books_table.setColumnWidth(0, 50)
        self.books_table.setColumnWidth(1, 150)
        self.books_table.setColumnWidth(2, 150)
        self.readers_table.setColumnWidth(0, 50)
        self.borrowing_table.setColumnWidth(0, 50)
        self.borrowing_table.setColumnWidth(1, 60)
        self.borrowing_table.setColumnWidth(2, 65)
        self.borrowing_table.setColumnWidth(3, 80)
        self.borrowing_table.setColumnWidth(4, 80)

    def getTableWidget(self, table_name):
        table_widget = None
        if table_name == BookTableName_:
            table_widget = self.books_table
        elif table_name == ReaderTableName_:
            table_widget = self.readers_table
        elif table_name == BorrowingTableName_:
            table_widget = self.borrowing_table
        return table_widget

    def initTableWid(self, table_name):
        table_attrs = util.getTableAttrs(table_name)
        table_attrs_ru = util.getTableAttrsRu(table_name)
        table_wid = self.getTableWidget(table_name)

        rows = get_page.getPage(self, table_name, 1, self.login_saved, self.password_saved)
        table_wid.setColumnCount(len(table_attrs))
        table_wid.setHorizontalHeaderLabels(table_attrs_ru)
        table_wid.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(table_attrs)):
                table_wid.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
        self.refreshPageLabel(table_name)

    def initTables(self):
        self.initTableWid(BookTableName_)
        self.initTableWid(ReaderTableName_)
        self.initTableWid(BorrowingTableName_)
        self.reformatTablesGui()

    def refreshTableWid(self, table_name):
        page_n = getattr(self, table_name+'_current_page')
        table_attrs = util.getTableAttrs(table_name)
        table_wid = self.getTableWidget(table_name)

        rows = get_page.getPage(self, table_name, page_n, self.login_saved, self.password_saved)
        table_wid.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(table_attrs)):
                table_wid.setItem(i, j, QTableWidgetItem(str(rows[i][j])))

    def refreshAllTableWid(self):
        self.refreshTableWid(BookTableName_)
        self.refreshTableWid(ReaderTableName_)
        self.refreshTableWid(BorrowingTableName_)

    def refreshPageLabel(self, table_name):
        if table_name == BookTableName_:
            self.book_page_label.setText(str(self.book_current_page))
        elif table_name == ReaderTableName_:
            self.reader_page_label.setText(str(self.reader_current_page))
        elif table_name == BorrowingTableName_:
            self.borrowing_page_label.setText(str(self.borrowing_current_page))
        elif table_name == BookBorrowingName_:
            self.borrowed_page_label.setText(str(self.b_b_current_page))

    def nextPage(self, table_name):
        if table_name == BookTableName_:
            self.book_current_page += 1
            self.refreshTableWid(table_name)
        elif table_name == ReaderTableName_:
            self.reader_current_page += 1
            self.refreshTableWid(table_name)
        elif table_name == BorrowingTableName_:
            self.borrowing_current_page += 1
            self.refreshTableWid(table_name)
        elif table_name == BookBorrowingName_:
            self.b_b_current_page += 1
            self.refreshBookBorrowTableWid(self.current_endp_mode)
        else:
            return
        self.refreshPageLabel(table_name)

    def backPage(self, table_name):
        if table_name == BookTableName_:
            if self.book_current_page > 1:
                self.book_current_page -= 1
                self.refreshTableWid(table_name)
        elif table_name == ReaderTableName_:
            if self.reader_current_page > 1:
                self.reader_current_page -= 1
                self.refreshTableWid(table_name)
        elif table_name == BorrowingTableName_:
            if self.borrowing_current_page > 1:
                self.borrowing_current_page -= 1
                self.refreshTableWid(table_name)
        elif table_name == BookBorrowingName_:
            if self.b_b_current_page > 1:
                self.b_b_current_page -= 1
                self.refreshBookBorrowTableWid(self.current_endp_mode)
        else:
            return
        self.refreshPageLabel(table_name)

    def setAttrsEditLayout(self, table_name):
        # clear layout
        for i in reversed(range(self.attrs_edit_hl.count())):
            self.attrs_edit_hl.itemAt(i).widget().setParent(None)

        table_attrs = util.getTableAttrs(table_name)
        table_attrs_ru = util.getTableAttrsRu(table_name)

        for attr_i in range(len(table_attrs)):
            attr_name = table_attrs[attr_i]
            attr_name_ru = table_attrs_ru[attr_i]

            label = QLabel(text=attr_name_ru + ':')
            label.setObjectName(table_name + '_' + attr_name + '_label')
            label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
            label.setMinimumSize(QSize(0, 35))
            self.attrs_edit_hl.addWidget(label)

            if attr_name == 'id':
                label_id = QLabel()
                label_id.setObjectName(table_name + '_' + attr_name + '_line')
                label_id.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
                label_id.setMinimumSize(QSize(0, 35))
                self.attrs_edit_hl.addWidget(label_id)
            else:
                line_edit = QLineEdit()
                line_edit.setObjectName(table_name + '_' + attr_name + '_line_edit')
                line_edit.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed))
                attr_line_size = getColumnSize(attr_name)
                line_edit.setFixedSize((QSize(attr_line_size, 35)))
                self.attrs_edit_hl.addWidget(line_edit)

    def getIdLineEdit(self, table_name):
        return self.findChild(QLabel, table_name + '_' + 'id' + '_line')

    def itemSelection(self, table_name):  # todo refactor
        if table_name == BookTableName_:
            if self.books_table.selectedIndexes():
                self.setAttrsEditLayout(table_name)
                self.selected_table = table_name

                self.getIdLineEdit(table_name).setText(
                    self.books_table.selectedIndexes()[0].data())
                for attr_i in range(1, len(BookAttrs_)):
                    self.findChild(QLineEdit, table_name + '_' + BookAttrs_[attr_i] + '_line_edit') \
                        .setText(self.books_table.selectedIndexes()[attr_i].data())
        elif table_name == ReaderTableName_:
            if self.readers_table.selectedIndexes():
                self.setAttrsEditLayout(table_name)
                self.selected_table = table_name

                self.getIdLineEdit(table_name).setText(
                    self.readers_table.selectedIndexes()[0].data())
                for attr_i in range(1, len(ReaderAttrs_)):
                    self.findChild(QLineEdit, table_name + '_' + ReaderAttrs_[attr_i] + '_line_edit') \
                        .setText(self.readers_table.selectedIndexes()[attr_i].data())
        elif table_name == BorrowingTableName_:
            if self.borrowing_table.selectedIndexes():
                self.setAttrsEditLayout(table_name)
                self.selected_table = table_name

                self.getIdLineEdit(table_name).setText(
                    self.borrowing_table.selectedIndexes()[0].data())
                for attr_i in range(1, len(BorrowingAttrs_)):
                    self.findChild(QLineEdit, table_name + '_' + BorrowingAttrs_[attr_i] + '_line_edit') \
                        .setText(self.borrowing_table.selectedIndexes()[attr_i].data())
        self.books_table.clearSelection()
        self.readers_table.clearSelection()
        self.borrowing_table.clearSelection()

        self.save_button.show()
        self.delete_button.show()

    def deleteClick(self):
        if self.selected_table is not None:
            id_ = self.getIdLineEdit(self.selected_table).text()
            delete_req.delete(self, self.selected_table, id_, self.login_saved, self.password_saved, self.xsrf)
            self.refreshTableWid(self.selected_table)

    def createJson(self, table_name):
        table_attrs = util.getTableAttrs(table_name)
        json = {
            'id': self.getIdLineEdit(table_name).text()}
        for attr_i in range(1, len(table_attrs)):
            field_text = self.findChild(QLineEdit, table_name + '_' + table_attrs[attr_i] + '_line_edit').text()
            if table_attrs[attr_i] == 'returned':
                if field_text.replace(' ', '') in ['Да', 'да', '1', '+']:
                    field_text = True
                else:
                    field_text = False
            json[table_attrs[attr_i]] = field_text
        return json

    def saveClick(self):
        idStr = self.getIdLineEdit(self.selected_table).text()
        if self.selected_table is not None and idStr.isdigit():
            json = self.createJson(self.selected_table)
            update.put(self, self.selected_table, json, self.login_saved, self.password_saved, self.xsrf)
            self.refreshTableWid(self.selected_table)

    def addClick(self, table_name):
        if table_name == BookTableName_:
            self.addBookForm.show()
        elif table_name == ReaderTableName_:
            self.addReaderForm.show()
        elif table_name == BorrowingTableName_:
            self.addBorrowingForm.show()

    def closeEvent(self, a0: QCloseEvent):
        super().closeEvent(a0)
        self.addBookForm.close()
        self.addReaderForm.close()
        self.addBorrowingForm.close()

    def searchClick(self):
        idStr = self.search_lineEdit.text()
        tableRu = self.table_comboBox.currentText()
        if tableRu == '':
            return
        tableName = util.get_key(TableNameRu_, tableRu)
        tableAttrs = util.getTableAttrs(tableName)
        tableWid = self.getTableWidget(tableName)
        resp = search.getOne(self, tableName, idStr, self.login_saved, self.password_saved)
        if resp['code'] == 200:
            row = resp['object']
            tableWid.setRowCount(1)
            for attr_i in range(len(tableAttrs)):
                tableWid.setItem(0, attr_i, QTableWidgetItem(str(row[attr_i])))

    def searchReset(self):
        self.refreshAllTableWid()
        self.search_lineEdit.clear()

    def statisticClick(self):
        self.stackedWidget.setCurrentIndex(1)
        self.resize(WindowWidthStats_, WindowHeight_)
        if self.isStatsTableInit:
            self.refreshStatsTableWid()
        else:
            self.initStatsTableWid()

    def setLabelBorrowed(self, endpoint_mode):
        if endpoint_mode == 'in':
            self.label_borrowed_header.setText('Невозвращённые книги, срок не подошёл')
        elif endpoint_mode == 'over':
            self.label_borrowed_header.setText('Невозвращённые книги, срок вышел')
        elif endpoint_mode == 'all':
            self.label_borrowed_header.setText('Выданные книги')

    def bookBorrowingClick(self, endpoint_mode):
        self.stackedWidget.setCurrentIndex(2)
        self.resize(WindowWidthBB_, WindowHeight_)
        self.setLabelBorrowed(endpoint_mode)
        if self.isBookBorrowTableInit:
            self.refreshBookBorrowTableWid(endpoint_mode)
        else:
            self.initBookBorrowTableWid(endpoint_mode)
        self.current_endp_mode = endpoint_mode

    # statistic page

    def returnStatisticClick(self):
        self.stackedWidget.setCurrentIndex(0)
        self.resize(WindowWidthMain_, WindowHeight_)

    def reformatStatsTableGui(self):
        self.table_statistic.setColumnWidth(1, 200)
        self.table_statistic.setColumnWidth(2, 200)
        self.table_statistic.setColumnWidth(3, 80)
        self.table_statistic.setColumnWidth(4, 80)

    def initStatsTableWid(self):
        attrs = StatisticAttrs_
        attrs_ru = StatisticAttrsRu_
        rows = get_statistic.getStatistic(self, '10', self.login_saved, self.password_saved)
        self.table_statistic.setColumnCount(len(attrs))
        self.table_statistic.setHorizontalHeaderLabels(attrs_ru)
        self.table_statistic.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(attrs)):
                self.table_statistic.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
        self.reformatStatsTableGui()
        self.isStatsTableInit = True

    def refreshStatsTableWid(self):
        limit = self.limit_spinBox.value()
        if self.period_checkBox.isChecked():
            dateStr = self.dateEdit.date().toString('yyyy-MM-dd')
            rows = get_statistic.getStatisticByPeriod(self, limit, dateStr, self.login_saved, self.password_saved)
        else:
            rows = get_statistic.getStatistic(self, limit, self.login_saved, self.password_saved)
        self.table_statistic.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(StatisticAttrs_)):
                self.table_statistic.setItem(i, j, QTableWidgetItem(str(rows[i][j])))

    # book_borrowing page
    def returnBorrowingClick(self):
        self.stackedWidget.setCurrentIndex(0)
        self.resize(WindowWidthMain_, WindowHeight_)
        self.current_endp_mode = None

    def reformatBBTableGui(self):
        self.table_book_borrowing.setColumnWidth(1, 200)
        self.table_book_borrowing.setColumnWidth(3, 200)

    def initBookBorrowTableWid(self, endpoint_mode):
        attrs = BookBorrowingAttrs_
        attrs_ru = BookBorrowingAttrsRu_
        table_wid = self.table_book_borrowing

        rows = get_b_b.getBookBorrowing(self, 1, endpoint_mode, self.login_saved, self.password_saved)
        table_wid.setColumnCount(len(attrs))
        table_wid.setHorizontalHeaderLabels(attrs_ru)
        table_wid.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(attrs)):
                table_wid.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
        self.refreshPageLabel(BookBorrowingName_)
        self.reformatBBTableGui()
        self.isBookBorrowTableInit = True

    def refreshBookBorrowTableWid(self, endpoint_mode: str):
        attrs = BookBorrowingAttrs_
        table_wid = self.table_book_borrowing
        rows = get_b_b.getBookBorrowing(self, self.b_b_current_page, endpoint_mode,
                                        self.login_saved, self.password_saved)
        table_wid.setRowCount(len(rows))
        for i in range(len(rows)):
            for j in range(len(attrs)):
                table_wid.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
        self.refreshPageLabel(BookBorrowingName_)
