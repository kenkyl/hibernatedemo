package com.kyle.hibernatedemo.services;

import com.kyle.hibernatedemo.models.Book;
import com.kyle.hibernatedemo.repositories.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    private BookRepository bookRepository;

    public List<Book> list() {
        return bookRepository.findAll();
    }
}
