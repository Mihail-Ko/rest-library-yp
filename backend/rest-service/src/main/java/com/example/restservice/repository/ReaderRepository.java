package com.example.restservice.repository;

import com.example.restservice.entity.ReaderEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ReaderRepository extends JpaRepository<ReaderEntity, Long> {
}