package com.example.restservice.repository;

import com.example.restservice.entity.BookBorrowingEntity;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;


public interface BookBorrowingRepository extends JpaRepository<BookBorrowingEntity, Long> {

    @Query(value = "SELECT book.id as book_id, book.name as book_name, book.author as author, " +
        "borrowing.returned as returned, borrowing.borrowing_date as borrowing_date, " +
        "borrowing.limit_date as limit_date, reader.id as reader_id, reader.name as reader_name, " +
        "borrowing.id as borrowing_id " +
        "FROM book " +
        "JOIN borrowing ON book.id = borrowing.book_id " +
        "JOIN reader ON borrowing.reader_id = reader.id;",
        countQuery = "SELECT count(*) FROM borrowing;",
        nativeQuery = true)
    Page<BookBorrowingEntity> getPage(Pageable pageable);

    @Query(value = "SELECT book.id as book_id, book.name as book_name, book.author as author, " +
        "borrowing.returned as returned, borrowing.borrowing_date as borrowing_date, " +
        "borrowing.limit_date as limit_date, reader.id as reader_id, reader.name as reader_name, " +
        "borrowing.id as borrowing_id " +
        "FROM book " +
        "JOIN borrowing ON book.id = borrowing.book_id " +
        "JOIN reader ON borrowing.reader_id = reader.id " +
        "WHERE borrowing.limit_date ~ E'^\\\\s*\\\\d{4}-\\\\d{2}-\\\\d{2}\\\\s*$' " +
        "AND CAST(limit_date AS DATE) >= CURRENT_DATE " +
        "AND borrowing.returned = false;",
        countQuery = "SELECT count(*) FROM borrowing;",
        nativeQuery = true)
    Page<BookBorrowingEntity> getCurrentInBorrowing(Pageable pageable);

    @Query(value = "SELECT book.id as book_id, book.name as book_name, book.author as author, " +
        "borrowing.returned as returned, borrowing.borrowing_date as borrowing_date, " +
        "borrowing.limit_date as limit_date, reader.id as reader_id, reader.name as reader_name, " +
        "borrowing.id as borrowing_id " +
        "FROM book " +
        "JOIN borrowing ON book.id = borrowing.book_id " +
        "JOIN reader ON borrowing.reader_id = reader.id " +
        "WHERE borrowing.limit_date ~ E'^\\\\s*\\\\d{4}-\\\\d{2}-\\\\d{2}\\\\s*$' " +
        "AND CAST(limit_date AS DATE) <= CURRENT_DATE " +
        "AND borrowing.returned = false;",
        countQuery = "SELECT count(*) FROM borrowing;",
        nativeQuery = true)
    Page<BookBorrowingEntity> getCurrentOverdue(Pageable pageable);
}