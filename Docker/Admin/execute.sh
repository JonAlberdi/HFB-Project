#!/usr/bin/env bash

cd etc/HFBapp/
python3 channel-join.py
python3 deploy-chaincode-v3.py
