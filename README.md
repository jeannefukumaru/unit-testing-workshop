# Unit Testing Workshop


### Setup

Build docker and start container
```shell
# build docker image
docker build . -t unit-testing-workshop

# start docker container
docker run -it -v $(pwd):/code -p 8888:8888 unit-testing-workshop

# get id of running container
docker ps 

# start another bash shell in the running container
docker exec -it <container-id> bash
```

Commands to be run inside the docker container
```shell
# add some color to your terminal
source bin/color_my_terminal.sh

# configure local venv on host
bin/configure_venv_locally.sh
# Configure your IDE to know where the python interpreter is

# run tests
nosetests

# run tests in watch mode
nosetests --with-watch

# start jupyter notebook
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

### Exercises

#### Exercise 1: Calculator

Implement the following functions in `src/calculator.py`:

```python
# subtract(a, b)
subtract(2, 1) --> 1

# multiply(a, b)
multiply(2, 3) --> 6

# divide(a, b)
divide(10, 5) --> 2

# bonus: handle rounding of floats to 2 precision points
divide(10, 3) --> 3.33
```

#### Exercise 2: ...



TODOs:
- find command for getting test coverage
- Create big jupyter script --> unit tests series of commits
- figure out how to store git credentials so that user don't have to type everyime