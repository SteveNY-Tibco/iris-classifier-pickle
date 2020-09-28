from tools import bash

def main():
  bash('curl -X POST -H "Content-Type: binary/octet-stream" -d @./newrelic.tar.gz http://127.0.0.1:10091/mops/projectmgr/pushProject/newrelic.tar.gz')
