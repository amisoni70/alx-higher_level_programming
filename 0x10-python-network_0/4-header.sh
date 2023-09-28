#!/bin/bash
# script that takes in a URL argument, sends a GET req & displays the body of response
curl -sH "X-School-User-Id: 98" "${1}"
