# Unit Testing Workshop


### Setup

```shell
# build docker image
docker build . -t unit-testing-workshop

# start docker container
docker run -it -v $(pwd):/home/unit-testing-workshop unit-testing-workshop 

# configure local venv on host
bin/configure_venv_locally.sh
# Configure your IDE to know where the python interpreter is
```


TODOs:
- find command for getting test coverage
