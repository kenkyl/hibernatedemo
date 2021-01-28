package com.kyle.hibernatedemo;

import com.kyle.hibernatedemo.services.InitObjectService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

@Component
public class InitComponent {

    private static final Logger LOG = LoggerFactory.getLogger(InitComponent.class);

    @Autowired
    private Environment environment;

    @Autowired
    private InitObjectService initObjectService;

    @PostConstruct
    public void init() {
        LOG.info("***INITIALIZING***");
        try {
            Boolean initFlag = environment.getProperty("LOAD_ON_STARTUP", Boolean.class);
            if (initFlag == true) {
                // pull data from MySQL and load Hibernate L2 cache (Redis)
                initObjectService.list();
            }
        } catch (NullPointerException ex) {
            LOG.info("$LOAD_ON_STARTUP not found");
            LOG.info(ex.getMessage());
        } catch (Exception ex) {
            LOG.info(ex.getMessage());
        }
    }
}
