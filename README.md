# DevOps Challenge
This repo contains suggested solution for DevOps Challenge.

## Requirements:
docker and docker-compose installed on linux machine


## Instructions:
clone the repo:

`git clone git@github.com:carmit246/challenge1.git`

locate directory:

`cd challenge1`

run solution:

`docker-compose up`


## Verify solution:
1.  use verification script:

`chmod +x verification.sh`

`./verification.sh`

2. verify manually:

`curl http://localhost:5000/secret`

`curl http://localhost:5000/health`
