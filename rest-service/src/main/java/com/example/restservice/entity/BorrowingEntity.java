package com.example.restservice.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "borrowing")
@Getter
@Setter
@NoArgsConstructor
public class BorrowingEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    private String limitDate;

    private boolean returned;

    private String borrowingDate;

    @ManyToOne
    @JoinColumn(name = "reader_id")
    private ReaderEntity reader;

    @ManyToOne
    @JoinColumn(name = "book_id")
    private BookEntity book;

}