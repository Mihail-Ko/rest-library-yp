package com.example.restservice.controller;

import com.example.restservice.service.StatisticService;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@Validated
@RestController
@RequestMapping("/statistic")
@RequiredArgsConstructor
public class StatisticController {

    private final StatisticService statisticService;

    @GetMapping
    @ResponseStatus(HttpStatus.OK)
    protected List<String> getBookStatistic(@RequestParam @Min(1) @Max(100) int limit) {
        return statisticService.getBookStatistic(limit);
    }

    @GetMapping("/period")
    @ResponseStatus(HttpStatus.OK)
    protected List<String> getBookStatisticByPeriod(@RequestParam @Min(1) @Max(100) int limit, @RequestParam String date) {
        return statisticService.getBookStatisticByPeriod(limit, date);
    }
}