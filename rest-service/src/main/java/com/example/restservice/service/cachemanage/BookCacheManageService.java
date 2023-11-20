package com.example.restservice.service.cachemanage;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Caching;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class BookCacheManageService {

    private final String cacheNameBook = "books";
    private final String cacheNameBookPage = "bookPages";

    @Caching(evict = {
        @CacheEvict(value = cacheNameBook, allEntries = true),
        @CacheEvict(value = cacheNameBookPage, allEntries = true)})
    public void clearCache() {
        log.info("Invalidate books cache");
    }
}