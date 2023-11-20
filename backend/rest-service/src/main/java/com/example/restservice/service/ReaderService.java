package com.example.restservice.service;

import com.example.restservice.mapper.ReaderMapper;
import com.example.restservice.model.ReaderModel;
import com.example.restservice.repository.ReaderRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.Caching;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;

@Service
@RequiredArgsConstructor
public class ReaderService extends CacheService {

    private final ReaderRepository readerRepository;
    private final ReaderMapper mapper;

    @CacheEvict(value = cacheNameReaderPage, allEntries = true)
    public ReaderModel addReader(ReaderModel reader) {
        return mapper.toModel(
            readerRepository.save(
                mapper.toEntity(reader)));
    }

    @Cacheable(value = cacheNameReaderPage, key = "#pageN", sync = true)
    public List<ReaderModel> getAll(int pageN) {
        return mapper.toModelList(
            readerRepository.findAll(
                    PageRequest.of(pageN - 1, 10))
                .getContent());
    }

    @Cacheable(value = cacheNameReader, key = "#id", sync = true)
    public ReaderModel getOne(long id) {
        return mapper.toModel(
            readerRepository.findById(id)
                .orElseThrow(NoSuchElementException::new));
    }

    @Caching(evict = {
        @CacheEvict(value = cacheNameReader, key = "#id"),
        @CacheEvict(value = cacheNameReaderPage, allEntries = true),
        @CacheEvict(value = cacheNameBorrowing, allEntries = true),
        @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)})
    public long delete(long id) {
        checkElementExist(id);
        readerRepository.deleteById(id);
        return id;
    }

    @Caching(
        put = @CachePut(value = cacheNameReader, key = "#reader.id"),
        evict = {
            @CacheEvict(value = cacheNameReaderPage, allEntries = true),
            @CacheEvict(value = cacheNameBorrowing, allEntries = true),
            @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)})
    public ReaderModel update(ReaderModel reader) {
        checkElementExist(reader.getId());
        return mapper.toModel(
            readerRepository.save(
                mapper.toEntity(reader)));
    }

    private void checkElementExist(long id) {
        if (readerRepository.findById(id).isEmpty())
            throw new NoSuchElementException();
    }
}