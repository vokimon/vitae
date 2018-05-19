#!/bin/bash

./setup.py test && python vitae/__main__.py davidgarcia-full > /dev/null && git diff --exit-code ./davidgarcia-full.tex ./davidgarcia-full.html && echo ALL OK!! || echo FAILURE!!!


