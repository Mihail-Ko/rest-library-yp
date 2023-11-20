package com.example.restservice.controller;

import com.example.restservice.entity.BookBorrowingEntity;
import com.example.restservice.service.BookBorrowingService;
import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/book-borrowing")
@RequiredArgsConstructor
public class BookBorrowingController {
    private final BookBorrowingService bookBorrowingService;

    @GetMapping("/all")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить сводку по выданным книгам")
    protected List<BookBorrowingEntity> getPage(@RequestParam int page) {
        return bookBorrowingService.getPage(page);
    }

    @GetMapping("/in")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить сводку по невозвращённым книгам, срок возврата не подошёл")
    protected List<BookBorrowingEntity> getCurrentInBorrowing(@RequestParam int page) {
        return bookBorrowingService.getCurrentInBorrowing(page);
    }

    @GetMapping("/over")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить сводку по невозвращённым книгам, срок вышел")
    protected List<BookBorrowingEntity> getCurrentOverdue(@RequestParam int page) {
        return bookBorrowingService.getCurrentOverdue(page);
    }
}
