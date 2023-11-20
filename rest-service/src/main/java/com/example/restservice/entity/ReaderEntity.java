package com.example.restservice.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.List;

@Entity
@Table(name = "reader")
@Getter
@Setter
@NoArgsConstructor
public class ReaderEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    private String name;

    private String surname;

    private String secondName;

    private String telephone;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "reader")
    private List<BorrowingEntity> borrowings;

}