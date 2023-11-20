package com.example.restservice.mapper;

import com.example.restservice.entity.BorrowingEntity;
import com.example.restservice.model.BorrowingModel;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

import java.util.List;

@Mapper(componentModel = "spring")
public interface BorrowingMapper {
    @Mapping(source = "reader.id", target = "readerId")
    @Mapping(source = "book.id", target = "bookId")
    BorrowingModel toModel(BorrowingEntity entity);

    @Mapping(source = "readerId", target = "reader.id")
    @Mapping(source = "bookId", target = "book.id")
    BorrowingEntity toEntity(BorrowingModel model);

    List<BorrowingModel> toModelList(List<BorrowingEntity> entities);
}