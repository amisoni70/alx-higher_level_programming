#!/bin/bash
# script that takes in a URL, sends a request to it & displays it in bytes
curl -s "$1" | wc -c
