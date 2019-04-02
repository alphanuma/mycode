#!/bin/bash
echo Enter a comment
read comment
cd ~/mycode
git add *
git commit -m "$comment"
git push origin master
