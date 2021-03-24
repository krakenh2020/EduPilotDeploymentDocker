# KRAKEN Education Pilot - Demo Deployment

Deployment of all server components needed to operate an university demonstrator.

Part of the **H2020 Project KRAKEN** and the **Verifiable Credentials for Student Mobility** project funded by TU Graz 
as a technologically enhanced administration (TEA) marketplace project.


## Startup

* to be able to start all containers, you need access to all required images (see below)
* don't forget to `docker login` without your GitHub credentials

```bash
sh generate_demo_keys.sh
docker-compose up --force-recreate
```


## Docker Images

* Connector: https://github.com/krakenh2020/EduPilotPrototype1
    - [kraken-edu_connector](https://github.com/krakenh2020/EduPilotPrototype1/packages/629143)
* API Platform: https://github.com/krakenh2020/EduPilotBackend
    - [kraken-edu_php](https://github.com/krakenh2020/EduPilotBackend/packages/629100)
    - [kraken-edu_frontend](https://github.com/krakenh2020/EduPilotBackend/packages/629067)
* Aries Agent: https://github.com/hyperledger/aries-framework-go
    - [agent-rest](https://github.com/hyperledger/aries-framework-go/packages/69982)
    - [webhook](https://github.com/hyperledger/aries-framework-go/blob/main/images/mocks/webhook/Dockerfile) 
      - at the moment, this image needs to be build locally: run `make sample-webhook-docker` in [aries-framework-go](https://github.com/hyperledger/aries-framework-go)
* Sidetree: *TODO*


## Exposed Services

* University connector: http://localhost:8001
* University API: http://localhost:8000/
* University Aries Agent: (with TLS)
    - API: https://localhost:8082/
    - Inbound: https://localhost:8081/
    - Webhook: http://localhost:8083/
* Student Aries Agent: (no TLS)
    - API: http://localhost:8092/
    - Inbound: http://localhost:8091/
    - Webhook: http://localhost:8093/


### To test mobile wallet of student:

* Agent: `http://10.0.2.2:8092`
* Agent WS: `ws://10.0.2.2:8092/ws`


