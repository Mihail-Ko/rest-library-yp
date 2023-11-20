package com.example.restservice.service;


import com.example.restservice.entity.BookBorrowingEntity;
import com.example.restservice.repository.BookBorrowingRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class BookBorrowingService {
    private final BookBorrowingRepository bookBorrowingRepo;

    public List<BookBorrowingEntity> getPage(int pageN) {
        return bookBorrowingRepo.getPage(
            PageRequest.of(pageN - 1, 10))
            .getContent();
    }

    public List<BookBorrowingEntity> getCurrentInBorrowing(int pageN) {
        return bookBorrowingRepo.getCurrentInBorrowing(
                PageRequest.of(pageN - 1, 10))
            .getContent();
    }

    public List<BookBorrowingEntity> getCurrentOverdue(int pageN) {
        return bookBorrowingRepo.getCurrentOverdue(
                PageRequest.of(pageN - 1, 10))
            .getContent();
    }
}
