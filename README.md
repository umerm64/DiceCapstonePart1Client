# DiceCapstonePart1Client
Client code for part1 of the capstone project

## Container orchestration
Dockerfile builds the image for the client container based on `python:3.8-alpine`
The docker-compose file creates the running instance of the client container along with the volume `servervol` mounted to `/serverdata`
The image tag can be obtained from the `.env` file
