package com.kyle.hibernatedemo;

import com.kyle.hibernatedemo.models.InitObject;
import com.kyle.hibernatedemo.services.InitObjectService;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

@RunWith(SpringRunner.class)
@SpringBootTest
public class InitObjectServiceUnitTest {
    @Autowired
    private InitObjectService initObjectService;

    @Test
    public void whenApplicationStarts_thenHibernateCreatesInitialRecords() {
        List<InitObject> initObjects = initObjectService.list();
        Assert.assertEquals(3, initObjects.size());
    }
}
