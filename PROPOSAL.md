# Proposal for Phase 2

## Performance improvements and scalability

As of now, we are using FastAPI, which is one of the fastest python web frameworks. However, we can increase the performance furthermore by using Ray Serve. Ray Serve is a scalable model-serving library for building online inference APIs. By using Ray Serve we can increase our performance up to 60 times.
Ray Serve usage can be referenced from [this](https://medium.com/distributed-computing-with-ray/how-to-scale-up-your-fastapi-application-using-ray-serve-c9a7b69e786) link.

## Implementing conversations

Since we are using MongoDB as our datastore, we propose to build a chat/conversation feature where the admin of the website can discuss regarding ad or analyses and work accordingly to increase advertisement performance.

## Providing recommendations for the ads

Since we are using MongoDB as our datastore, we propose building a collaborative filtering recommendation system. We are saving data in such a way that existing services can be extended to support this functionality.

## Support for targeted ad campaigns

We can target ads based on the demographics as we are collecting the location. Based on the location and analysis we already did we can target the ads for a specific set population.
