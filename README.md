# interview

Coding Interview problems

## Data Ingestor

We have this micro-service that can accept JSON data from a city. You can imagine it might store this data in a database or do some processing on it as part of an ML pipeline. Currently it only can accept data in a JSON format as well as return it in a JSON format. We have customers that want to be able to send and receive the data in the CSV format as well.

Our job is to extend this service to be able to accept and return CSV data, as well as write unit-tests for it.

### Stretch goals

- We internally use the Unix epoch time for our timestamps, so we'd like to convert the "time" column into that format internally.
