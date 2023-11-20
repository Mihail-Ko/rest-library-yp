package com.example.restservice.repository;

import com.example.restservice.entity.BorrowingEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BorrowingRepository extends JpaRepository<BorrowingEntity, Long> {
}