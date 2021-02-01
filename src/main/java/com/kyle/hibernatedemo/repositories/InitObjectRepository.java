package com.kyle.hibernatedemo.repositories;

import com.kyle.hibernatedemo.models.InitObject;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.QueryHints;
import org.springframework.stereotype.Repository;

import javax.persistence.QueryHint;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static org.hibernate.jpa.QueryHints.HINT_CACHEABLE;

@Repository
public interface InitObjectRepository extends JpaRepository <InitObject, Long> {

    @QueryHints(@QueryHint(name = HINT_CACHEABLE, value = "true"))
    @Override
    public List<InitObject> findAll();

//    @QueryHints(@QueryHint(name = HINT_CACHEABLE, value = "true"))
//    public List<InitObject> findAllCustom() {
//        List<InitObject> objects = new ArrayList<InitObject>();
//        return objects;
//    }
}
