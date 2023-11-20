package com.example.restservice.model;

import lombok.Getter;
import lombok.Setter;

import java.io.Serializable;


@Getter
@Setter
public class ReaderModel implements Serializable {
    private long id;
    private String name;
    private String surname;
    private String secondName;
    private String telephone;
}