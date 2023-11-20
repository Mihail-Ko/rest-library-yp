package com.example.restservice.entity;


import jakarta.persistence.Entity;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import jakarta.persistence.*;
import java.io.Serializable;


@Entity
@Getter
@Setter
@NoArgsConstructor
public class BookBorrowingEntity implements Serializable {
    private long book_id;
    private String book_name;
    private String author;
    @Id
    private long borrowing_id;
    private Boolean returned;
    private String borrowing_date;
    private String limit_date;
    private long reader_id;
    private String reader_name;
}