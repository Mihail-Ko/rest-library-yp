package com.example.restservice.service;

import com.example.restservice.repository.BookStatisticRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
@RequiredArgsConstructor
public class StatisticService {

    private final BookStatisticRepository bookStatisticRep;

    public List<String> getBookStatistic(int limit) {
        return bookStatisticRep.getTopBooks(limit);
    }

    public List<String> getBookStatisticByPeriod(int limit, String periodDate) {
        return bookStatisticRep.getTopBooksByPeriod(limit, periodDate);
    }
}