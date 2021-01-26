package com.kyle.hibernatedemo;

import com.kyle.hibernatedemo.models.InitObject;
import com.kyle.hibernatedemo.services.InitObjectService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import static java.lang.Long.valueOf;

@RestController
public class InitObjectController {
    @Autowired
    InitObjectService initObjectService;

    @RequestMapping("/index")
    public String healthCheck() {
        return "I'm alive!";
    }

    @RequestMapping("/init")
    public String getAll() {
        Long start = System.nanoTime();
        List<InitObject> res = initObjectService.list();
        Long end = System.nanoTime();
        Long time = end - start;
        return String.format("time: %s\nobjects: %s", time.toString(), "fetched");
        //return String.format("time: %s\nobjects: %s", time.toString(), res.toString());
    }

    @RequestMapping("/init/{id}")
    public String getOne(@PathVariable String id) {
        Long start = System.nanoTime();
        InitObject res = initObjectService.findOne(valueOf(id));
        Long end = System.nanoTime();
        Long time = end - start;

        return String.format("time: %s\nobject: %s", time.toString(), res.toString());
    }

}
