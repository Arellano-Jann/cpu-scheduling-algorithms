#!/bin/bash

# Runs vmstat, top and free and writes the output to a file

vmstat > vmstat.txt
top -b -n 2 > top.txt
free > free.txt