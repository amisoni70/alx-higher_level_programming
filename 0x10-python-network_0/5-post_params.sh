#!/bin/bash
# script that takes in a URL, sends a POST req to the passed URL & displays the body of response
curl -s X POST -d "email=test@gmail.com&subject=I will always be here for PLD" ${1}
