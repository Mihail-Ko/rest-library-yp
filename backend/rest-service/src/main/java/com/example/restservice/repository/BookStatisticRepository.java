package com.example.restservice.repository;

import com.example.restservice.entity.BookEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface BookStatisticRepository extends JpaRepository<BookEntity, Long> {
    @Query(value = "SELECT book.*, COUNT(borrowing.book_id) AS borrowing_count " +
        "FROM book " +
        "JOIN borrowing ON book.id = borrowing.book_id " +
        "GROUP BY book.id " +
        "ORDER BY borrowing_count DESC " +
        "LIMIT :limit ;",
        nativeQuery = true)
    List<String> getTopBooks(int limit);

    @Query(value = "SELECT book.*, COUNT(borrowing.book_id) AS borrowing_count " +
        "FROM book " +
        "JOIN borrowing ON book.id = borrowing.book_id " +
        "WHERE TO_DATE(borrowing.borrowing_date, 'YYYY-MM-DD') > CAST(:periodDate AS DATE) " +
        "GROUP BY book.id " +
        "ORDER BY borrowing_count DESC " +
        "LIMIT :limit ;",
        nativeQuery = true)
    List<String> getTopBooksByPeriod(int limit, String periodDate);
}