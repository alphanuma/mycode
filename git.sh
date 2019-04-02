#!/bin/bash

read comment
cd ~/mycode
git add *
echo "time to add your comments"
git commit -m "$comment"
git push origin master
