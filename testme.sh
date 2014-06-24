#!/bin/bash

./UnitTests.py && ./davidgarcia-full.py > /dev/null && git diff --exit-code ./davidgarcia-full.tex ./davidgarcia-full.html && echo ALL OK!! || echo FAILURE!!!


