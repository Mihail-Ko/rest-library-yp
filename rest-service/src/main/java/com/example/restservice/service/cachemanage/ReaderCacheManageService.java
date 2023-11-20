package com.example.restservice.service.cachemanage;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Caching;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class ReaderCacheManageService {

    private final String cacheNameReader = "readers";
    private final String cacheNameReaderPage = "readerPages";

    @Caching(evict = {
        @CacheEvict(value = cacheNameReader, allEntries = true),
        @CacheEvict(value = cacheNameReaderPage, allEntries = true)})
    public void clearCache() {
        log.info("Invalidate readers cache");
    }
}