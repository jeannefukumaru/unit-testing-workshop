# Unit Testing Workshop


### Setup

Build docker and start container
```shell
# build docker image
docker build . -t unit-testing-workshop

# start docker container
docker run -it -v $(pwd):/code -p 8888:8888 unit-testing-workshop

# configure local venv on host. This is a workaround to give us intellisense and code completion when we write code
bin/configure_venv_locally.sh
# After running the command, on your IDE, go and configure it to tell it that the python interpreter is in .venv-local/
# More instructions here: https://github.com/davified/ci-workshop-app/blob/master/docs/FAQs.md#ide-configuration
```

Commands to be run inside the docker container
```shell
# add some color to your terminal
source bin/color_my_terminal.sh

# run tests
nosetests

# run tests in watch mode
nosetests --with-watch

# start jupyter notebook
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

When you reach the point in the workshop where you need another start another bash shell in the running container, run the following commands on your host machine:
```shell
# get id of running container
docker ps 

# start another bash shell in the running container
docker exec -it <container-id> bash
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

#### Exercise 2: Adding tests and refactoring a notebook

We will refactor [this notebook](notebooks/sklearn-nlp-pipeline-before-refactoring.ipynb) by creating and extracting functions and adding tests.
