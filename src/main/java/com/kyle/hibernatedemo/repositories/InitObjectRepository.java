package com.kyle.hibernatedemo.repositories;

import com.kyle.hibernatedemo.models.InitObject;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface InitObjectRepository extends JpaRepository <InitObject, Long> {

}
