package com.example.restservice.exception;

import jakarta.validation.ConstraintViolationException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.dao.InvalidDataAccessApiUsageException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;

import java.util.NoSuchElementException;

@Slf4j
@RestControllerAdvice
public class DefaultAdvice {

    @ExceptionHandler(NoSuchElementException.class)
    public ResponseEntity<String> notFoundHandler(NoSuchElementException noSuchElementExc) {
        log.info(
            String.valueOf(noSuchElementExc));
        return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body("Элемент не найден");
    }

    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    public ResponseEntity<String> methodNotSupportedHandler(HttpRequestMethodNotSupportedException methodNotSupportedExc) {
        log.info(
            String.valueOf(methodNotSupportedExc));
        return ResponseEntity
            .status(HttpStatus.METHOD_NOT_ALLOWED)
            .body("Метод не поддерживается");
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<String> messageHandler(HttpMessageNotReadableException notReadableExc) {
        log.info(
            String.valueOf(notReadableExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Ошибка в теле запроса");
    }

    @ExceptionHandler(MissingServletRequestParameterException.class)
    public ResponseEntity<String> parameterHandler(MissingServletRequestParameterException parameterExc) {
        log.info(
            String.valueOf(parameterExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Ошибка в параметре запроса");
    }

    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ResponseEntity<String> argumentTypeHandler(MethodArgumentTypeMismatchException argumentTypeExc) {
        log.info(
            String.valueOf(argumentTypeExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Ошибка в параметре запроса");
    }

    @ExceptionHandler(IllegalArgumentException.class)
    public ResponseEntity<String> argumentHandler(IllegalArgumentException argumentExc) {
        log.info(
            String.valueOf(argumentExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Номер страницы должен быть больше 0");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> exceptionHandler(Exception exception) {
        exception.printStackTrace();
        return ResponseEntity
            .status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body("Ошибка сервера");
    }

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<String> validationHandler(ConstraintViolationException validationExc) {
        log.info(
            String.valueOf(validationExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Недопустимое значение параметра");
    }

    @ExceptionHandler(DataIntegrityViolationException.class)
    public ResponseEntity<String> dataIntegrityValidationHandler(DataIntegrityViolationException validationExc) {
        log.info(
            String.valueOf(validationExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Недопустимое значение параметра");
    }
    @ExceptionHandler(InvalidDataAccessApiUsageException.class)
    public ResponseEntity<String> invalidDataAccessApiUsageExcHandler(InvalidDataAccessApiUsageException validationExc) {
        log.info(
            String.valueOf(validationExc));
        return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body("Недопустимое значение");
    }

}
