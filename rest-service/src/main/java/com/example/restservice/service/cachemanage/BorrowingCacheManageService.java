package com.example.restservice.service.cachemanage;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Caching;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class BorrowingCacheManageService {

    private final String cacheNameBorrowing = "borrowings";
    private final String cacheNameBorrowingPage = "borrowingPages";

    @Caching(evict = {
        @CacheEvict(value = cacheNameBorrowing, allEntries = true),
        @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)})
    public void clearCache() {
        log.info("Invalidate borrowing cache");
    }
}