#!/bin/sh
wrk -t12 -c64 -d15s -s ./benchmark/post.lua http://localhost:8080/
