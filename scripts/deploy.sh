#!/usr/bin/env bash

scp scripts/install_requirements.sh interview@52.91.133.149:install_requirements.sh
scp scripts/build_and_run_app.sh interview@52.91.133.149:build_and_run_app.sh
ssh interview@52.91.133.149 "sudo /home/interview/install_requirements.sh"
ssh interview@52.91.133.149 /home/interview/build_and_run_app.sh