package com.kyle.hibernatedemo.repositories;

import com.kyle.hibernatedemo.models.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookRepository extends JpaRepository <Book, Long> {

}
