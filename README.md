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

# run tests
python -m unittest discover -s src/
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