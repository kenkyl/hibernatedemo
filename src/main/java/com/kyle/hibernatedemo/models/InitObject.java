package com.kyle.hibernatedemo.models;

import org.hibernate.annotations.CacheConcurrencyStrategy;

import javax.persistence.Cacheable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@Cacheable
@org.hibernate.annotations.Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class InitObject {

    @Id
    @GeneratedValue
    private Long id;
    private String value1;
    private String value2;
    private String value3;
    private String value4;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getValue1() {
        return value1;
    }

    public void setValue1(String value1) {
        this.value1 = value1;
    }

    public String getValue2() {
        return value2;
    }

    public void setValue2(String value2) {
        this.value2 = value2;
    }

    public String getValue3() {
        return value1;
    }

    public void setValue3(String value1) {
        this.value1 = value1;
    }

    public String getValue4() {
        return value2;
    }

    public void setValue4(String value2) {
        this.value2 = value2;
    }
}
