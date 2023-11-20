package com.example.restservice.controller;


import com.example.restservice.model.BorrowingModel;
import com.example.restservice.service.BorrowingService;
import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/borrowing")
@RequiredArgsConstructor
public class BorrowingController {

    private final BorrowingService borrowingService;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Добавить выдачу")
    protected BorrowingModel addBorrowing(@RequestBody BorrowingModel borrowing) {
        return borrowingService.addBorrowing(borrowing);
    }

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить страницу выдачи")
    protected List<BorrowingModel> getBorrowing(@RequestParam int page) {
        return borrowingService.getAll(page);
    }

    @GetMapping("/{id}")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить выдачу по id")
    protected BorrowingModel getOneBorrowing(@PathVariable long id) {
        return borrowingService.getOne(id);
    }


    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Удалить выдачу по id")
    protected String deleteBorrowing(@PathVariable long id) {
        return "Удалена выдача с id " + borrowingService.delete(id);
    }

    @PutMapping()
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Обновить выдачу")
    protected BorrowingModel updateBorrowing(@RequestBody BorrowingModel borrowing) {
        return borrowingService.update(borrowing);
    }

}