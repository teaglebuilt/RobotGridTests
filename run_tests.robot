## SUITE NAME
--name UI Prod Tests

## SETTINGS
--pythonpath ./lib
--pythonpath .

# LOG LEVEL
# --loglevel DEBUG
--loglevel INFO

# put all logs into directory
--outputdir reports
# --timestampoutputs
--debugfile debug.logenv

-v BROWSER:firefox
-v DISPLAY_WIDTH:1920
-v DISPLAY_HEIGHT:1080


## PROXY
-v USE_PROXY:False
-v PROXY_TYPE:socks
-v PROXY_HOST:localhost
-v PROXY_PORT:9999

## VARIABLES
-v REPO_PATH:data/ui_elements.yml
-V config.py

## TEST SUITES
./tests/