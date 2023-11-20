package com.example.restservice.model;

import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;

@Getter
@Setter
public class BorrowingModel implements Serializable {
    private long id;
    private Boolean returned;
    private String borrowingDate;
    private String limitDate;
    private long bookId;
    private long readerId;
}
