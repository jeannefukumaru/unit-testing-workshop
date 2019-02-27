#!/usr/bin/env bash

which brew
if [ $? -ne 0 ]; then
  echo "INFO: Installing homebrew"
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

echo "INFO: Installing docker if not installed"
command -v docker >/dev/null 2>&1 || brew cask install docker 

open --background -a Docker
while ! docker system info > /dev/null 2>&1; do sleep 1 && echo "[INFO] Waiting for docker daemon startup to complete..."; done

echo "Building unit-testing-workshop docker image"

docker build . -t unit-testing-workshop

echo "Done"