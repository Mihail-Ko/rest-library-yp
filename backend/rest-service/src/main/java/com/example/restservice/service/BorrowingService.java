package com.example.restservice.service;

import com.example.restservice.mapper.BorrowingMapper;
import com.example.restservice.model.BorrowingModel;
import com.example.restservice.repository.BorrowingRepository;
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
public class BorrowingService extends CacheService {

    private final BorrowingRepository borrowingRepository;
    private final BorrowingMapper mapper;

    @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)
    public BorrowingModel addBorrowing(BorrowingModel borrowing) {
        return mapper.toModel(
            borrowingRepository.save(
                mapper.toEntity(borrowing)));
    }

    @Cacheable(value = cacheNameBorrowingPage, key = "#pageN", sync = true)
    public List<BorrowingModel> getAll(int pageN) {
        return mapper.toModelList(
            borrowingRepository.findAll(
                    PageRequest.of(pageN - 1, 10))
                .getContent());
    }

    @Cacheable(value = cacheNameBorrowing, key = "#id", sync = true)
    public BorrowingModel getOne(long id) {
        return mapper.toModel(
            borrowingRepository.findById(id)
                .orElseThrow(NoSuchElementException::new));
    }

    @Caching(evict = {
        @CacheEvict(value = cacheNameBorrowing, key = "#id"),
        @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)})
    public long delete(long id) {
        checkElementExist(id);
        borrowingRepository.deleteById(id);
        return id;
    }

    @Caching(
        put = @CachePut(value = cacheNameBorrowing, key = "#borrowing.id"),
        evict = @CacheEvict(value = cacheNameBorrowingPage, allEntries = true))
    public BorrowingModel update(BorrowingModel borrowing) {
        checkElementExist(borrowing.getId());
        return mapper.toModel(
            borrowingRepository.save(
                mapper.toEntity(borrowing)));
    }

    private void checkElementExist(long id) {
        if (borrowingRepository.findById(id).isEmpty())
            throw new NoSuchElementException();
    }
}