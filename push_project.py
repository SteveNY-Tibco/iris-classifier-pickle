from tools import bash

def main():
  try:
    bash('curl --header "Content-Type:application/octet-stream" --trace-ascii debugdump.txt --data-binary @./SteveNY-Tibco_iris-classifier-pickle.tar.gz http://127.0.0.1:10091/mops/projectmgr/pushProject/SteveNY-Tibco_iris-classifier-pickle.tar.gz')
    return 0
  except:
    return 1
  finally:
    print('Finally: cleanup')
