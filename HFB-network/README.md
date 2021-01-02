# HFB-network

## SET ENVIRONMENTAL VARIABLES

export FABRIC_VERSION=1.4.6
export FABRIC_CA_VERSION=1.4.6

## CASE SOLO WITH GOLEVELDB

1. Generate cryptographic material

   - cd crypto-material/config_solo
   - ./generate.sh

2. Deploy HFB network

   - cd networks/2org1peergoleveldb_solo
   - docker-compose up -d

## CASE SOLO WITH COUCHDB

1. Generate cryptographic material

   - cd crypto-material/config_solo
   - ./generate.sh

2. Deploy HFB network

   - cd networks/2org1peercouchdb_solo
   - docker-compose up -d

## CASE RAFT WITH GOLEVELDB

1. Generate cryptographic material

   - cd crypto-material/config_raft
   - ./generate.sh

2. Deploy HFB network

   - cd networks/2org1peergoleveldb_raft
   - docker-compose up -d

## CASE KAFKA WITH GOLEVELDB

1. Generate cryptographic material

   - cd crypto-material/config_kafka
   - ./generate.sh

2. Deploy HFB network

   - cd networks/2org1peergoleveldb_kafka
   - docker-compose up -d

## CASE SOLO 2ORG WITH GOLEVELDB

1. Set-up environmental variables, adding to PATH, binary configtxgen:

   - e.g.: cp -r configtxgen /usr/bin/local

2. Deploy HFB network

   - cd networks/2org2peergoleveldb
   - docker-compose up -d

3. Join Peers to Channel

   - cd app
   - python3 channel-join.py

4. Instale chaincode/Instantiate chaincode

   - cd app
   - python3 deploy-chaincode.py

5. Invoke transactions

   - cd app
   - python3 invoke.py

6. Query transactions

   - cd app
   - python3 query.py

---

| chaincode          | channel-join | deploy-chaincode | invoke | query  |
| ------------------ | ------------ | ---------------- | ------ | ------ |
| example_cc         | v1           | v1               | v1     | v1     |
| ------------------ | ------------ | ---------------- | ------ | ------ |
| registration_cc_v1 | v2           | v2               | v2     | v2     |
| ------------------ | ------------ | ---------------- | ------ | ------ |
| registration_cc_v2 | v3           | v3               | v3     | v3     |

---
