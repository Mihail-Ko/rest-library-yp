package com.example.restservice.mapper;

import com.example.restservice.entity.ReaderEntity;
import com.example.restservice.model.ReaderModel;
import org.mapstruct.Mapper;

import java.util.List;

@Mapper(componentModel = "spring")
public interface ReaderMapper {
    ReaderModel toModel(ReaderEntity entity);

    ReaderEntity toEntity(ReaderModel model);

    List<ReaderModel> toModelList(List<ReaderEntity> entities);
}