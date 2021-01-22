package com.kyle.hibernatedemo;

import com.kyle.hibernatedemo.models.Book;
import com.kyle.hibernatedemo.services.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
public class BooksController {
    @Autowired
    BookService bookService;

    @RequestMapping("/healthCheck")
    public String healthCheck() {
        return "I'm alive!";
    }

    @RequestMapping("/books")
    public String get() {
        Long start = System.nanoTime();
        List<Book> res = bookService.list();
        Long end = System.nanoTime();
        Long time = end - start;

        return String.format("time: %s\nbooks: %s", time.toString(), res.toString());
    }
}
