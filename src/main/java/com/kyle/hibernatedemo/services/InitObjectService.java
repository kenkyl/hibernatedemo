package com.kyle.hibernatedemo.services;

import com.kyle.hibernatedemo.models.InitObject;
import com.kyle.hibernatedemo.repositories.InitObjectRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class InitObjectService {
    @Autowired
    private InitObjectRepository initObjectRepository;

    public List<InitObject> list() {
        return initObjectRepository.findAll();
    }
    
    public InitObject findOne(long id) {
        Optional<InitObject> initObjectOptional = initObjectRepository.findById(id);
        if (initObjectOptional.isPresent()) {
            System.out.println("****GOT IT");
            return initObjectOptional.get();
        } else {
            System.out.println("****NOT****GOT IT");
            return null;
        }
    }
}
