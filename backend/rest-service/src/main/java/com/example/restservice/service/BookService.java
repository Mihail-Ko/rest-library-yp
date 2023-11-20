package com.example.restservice.service;

import com.example.restservice.mapper.BookMapper;
import com.example.restservice.model.BookModel;
import com.example.restservice.repository.BookRepository;
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
public class BookService extends CacheService {

    private final BookRepository bookRepository;
    private final BookMapper mapper;

    @CacheEvict(value = cacheNameBookPage, allEntries = true)
    public BookModel addBook(BookModel book) {
        return mapper.toModel(
            bookRepository.save(
                mapper.toEntity(book)));
    }

    @Cacheable(value = cacheNameBookPage, key = "#pageN", sync = true)
    public List<BookModel> getAll(int pageN) {
        return mapper.toModelList(
            bookRepository.findAll(
                    PageRequest.of(pageN - 1, 10))
                .getContent());
    }

    @Cacheable(value = cacheNameBook, key = "#id", sync = true)
    public BookModel getOne(long id) {
        return mapper.toModel(
            bookRepository.findById(id)
                .orElseThrow(NoSuchElementException::new));
    }

    @Caching(evict = {
        @CacheEvict(value = cacheNameBook, key = "#id"),
        @CacheEvict(value = cacheNameBookPage, allEntries = true),
        @CacheEvict(value = cacheNameBorrowing, allEntries = true),
        @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)
    })
    public long delete(long id) {
        checkElementExist(id);
        bookRepository.deleteById(id);
        return id;
    }

    @Caching(
        put = @CachePut(value = cacheNameBook, key = "#book.id"),
        evict = {
            @CacheEvict(value = cacheNameBookPage, allEntries = true),
            @CacheEvict(value = cacheNameBorrowing, allEntries = true),
            @CacheEvict(value = cacheNameBorrowingPage, allEntries = true)})
    public BookModel update(BookModel book) {
        checkElementExist(book.getId());
        return mapper.toModel(
            bookRepository.save(
                mapper.toEntity(book)));
    }

    private void checkElementExist(long id) {
        if (bookRepository.findById(id).isEmpty())
            throw new NoSuchElementException();
    }
}