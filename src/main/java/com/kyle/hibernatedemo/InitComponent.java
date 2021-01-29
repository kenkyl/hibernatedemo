package com.kyle.hibernatedemo;

import com.kyle.hibernatedemo.models.InitObject;
import com.kyle.hibernatedemo.services.InitObjectService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.List;

@Component
public class InitComponent {

    private static final Logger LOG = LoggerFactory.getLogger(InitComponent.class);

    @Autowired
    private Environment environment;

    @Autowired
    private InitObjectService initObjectService;

    @PostConstruct
    public void init() {
        LOG.info("***Initial data load starting...***");
        try {
            Boolean initFlag = environment.getProperty("LOAD_ON_STARTUP", Boolean.class);
            if (initFlag == true) {
                // pull data from MySQL and load Hibernate L2 cache (Redis)
                Long start = System.nanoTime();
                initObjectService.list();
                Long end = System.nanoTime();
                Long time = end - start;
                LOG.info(String.format("***Initialize data load complete. Time estimate: %s***", time.toString()));
            }
        } catch (NullPointerException ex) {
            LOG.info("***$LOAD_ON_STARTUP not found***");
            LOG.info(ex.getMessage());
        } catch (Exception ex) {
            LOG.info(ex.getMessage());
        }
    }
}
