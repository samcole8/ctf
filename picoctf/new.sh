#!/bin/bash

mkdir $1
mkdir $1/content
touch $1/content/readme.txt $1/flag

echo $2 > $1/content/readme.txt
