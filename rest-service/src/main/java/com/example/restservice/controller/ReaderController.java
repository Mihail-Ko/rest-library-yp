package com.example.restservice.controller;

import com.example.restservice.model.ReaderModel;
import com.example.restservice.service.ReaderService;
import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/reader")
@RequiredArgsConstructor
public class ReaderController {

    private final ReaderService readerService;

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    @Operation(summary = "Добавить читателя")
    protected ReaderModel addReader(@RequestBody ReaderModel reader) {
        return readerService.addReader(reader);
    }

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить страницу списка читателей")
    protected List<ReaderModel> getReaders(@RequestParam int page) {
        return readerService.getAll(page);
    }

    @GetMapping("/{id}")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Получить читателя по id")
    protected ReaderModel getOneReader(@PathVariable long id) {
        return readerService.getOne(id);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Удалить читателя по id")
    protected String deleteReader(@PathVariable long id) {
        return "Удален читатель с id " + readerService.delete(id);
    }

    @PutMapping()
    @ResponseStatus(HttpStatus.OK)
    @Operation(summary = "Обновить читателя")
    protected ReaderModel updateReader(@RequestBody ReaderModel reader) {
        return readerService.update(reader);
    }

}

