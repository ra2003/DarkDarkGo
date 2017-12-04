# MGMT Database

## SQL Schema Example

```
link
    ----------------------------------------------------------------
   | index  | link                      | chunk_id    | state       |
   | SERIAL | VARCHAR(255)              | VARCHAR(22) | VARCHAR(22) |
   |        | PRIMARY                   | REF         |             |
    ----------------------------------------------------------------
   | 1      | https://www.example_1.com | 1           | crawled     |
   | 2      | https://www.example_2.com | 1           | crawled     | 
   | 3      | https://www.example_3.com | 1           | crawled     | 
   | 4      | https://www.example_4.com | 1           | crawled     |
   | 5      | https://www.example_5.com | 1           | crawled     |  
   | 6      | https://www.example_6.com | None        | None        | 
    ----------------------------------------------------------------

chunk
    -------------------
   | index  | id       |
   | SERIAL | INT      |
   |        | PRIMARY  |
    -------------------
   | 1      | 1        |
    -------------------
   
host
    -------------------------------------------------------------------------
   | index  | host               | type           | state      | health      |
   | SERIAL | VARCHAR(22)        | VARCHAR(22)    | VARCHAR(22)| VARCHAR(22) |   
   |        | PRIMARY            |                |            |             |   
    -------------------------------------------------------------------------
   | 1      | 10.10.127.100:5000 | Crawler        | online     | healthy      |
   | 2      | 10.10.127.101:5000 | Index Builider | online     | healthy      |
   | 3      | 10.10.127.102:5000 | Index Server   | online     | healthy      |
    -------------------------------------------------------------------------

crawler
    ------------------------------------------------------
   | index  | chunk_id | C_host             | C_task      |
   | SERIAL | INT      | VARCHAR(22)        | VARCHAR(22) |
   |        | REF      | REF                |             | 
    ------------------------------------------------------
   | 1      | 1        | 10.10.127.100:5000 | crawled     |
    ------------------------------------------------------

index_builder
    ------------------------------------------------------
   | index  | chunk_id | IB_host            | IB_task     | 
   | SERIAL | INT      | VARCHAR(22)        | VARCHAR(22) | 
   |        | REF      | REF                |             |
    ------------------------------------------------------
   | 1      | 1        | 1                  | building    |
    ------------------------------------------------------

index_server
    ------------------------------------------------
   | Index  | row   | chunk_id | IS_host            | 
   | SERIAL | INT   | INT      | VARCHAR(22)        | 
   |        |       | REF      | REF                |
    ------------------------------------------------
   | 1      | 1     | 100      | 10.10.127.102:5000 |
   | 2      | 2     | 101      | 10.10.127.102:5000 |
   | 3      | 3     | 102      | 10.10.127.102:5000 |
    ------------------------------------------------
```


### Logic

#### Crawler
- When insert link to Link relation, default chunk_id is None and state is pending
- When Crawler request links:
- - We get the first 5 links where chunk_id is None and state is pending
  - Assign a new chunk_id for these links and insert it to Chunk relation 
  - Update chunk_id and set links state to crawling in Link relation
  - Insert that chunk_id to Crawler relation that host and set task to crawling
- If Crawler finish crawling without any error, they send us chunk_id with crawled state.
  - Update that chunk_id task to crawled in Crawler relation
  - Update corresponding links to crawled in Link relation
  - Insert that chunk_id to Index Builder relation, default IB's host and default task is None
- Otherwise:
  - Crawler send us a link with error state. 
  - We mark it as error in Link relation and use that to find out which chunk_id is 
  so we can return them a new one with pending state with the same chunk_id
  - Under no circumstance delete a link, only mark them as error.

#### Index Builder
- When Index Builder request chunk metadata from us:
  - We get the first 5 chunk_id where task is None
  - Give them chunk_id with Crawler's host
  - Update Index Builder's host and set task to building
- If Index Builder finish indexing without any error, they send us chunk_id with built state
  - We mark them as built in Index Builder relation
  - TODO: ASSIGN TASK TO SERVER HERE 
- Otherwise:
  - They send us a chunk_id with error state.
  - We mark them as error.
  - Unlike Crawler, they don't need request new chunk_ids for broken one.
  They will get 5 chunks every time they ask us. 

### Index Server
- If a chunk_id is successfully crawled and built, insert it to Index Server relation.
- TODO: CHOOSE A DISTRIBUTING ALGORITHM

### How to install on Mac:
- Install [Posgres.app](https://postgresapp.com)
- `sudo -u <username> createdb -O <username> mgmt_db`
- `./import.sh`