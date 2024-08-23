# Instruction to execute this in Mac or Linux OS
run following commands to excecute the test cases.
create VirtualEnv using below command:
  python/python3 -m venv /path/envname

After successfully creating the venv activate using below command
    /path/envname/bin/activate

Install the requiremnts in the venv using following command:

  python/python3 -m pip install -r requirements.txt

To excute the test cases:

  pytest func_test.py -v > test_output.txt

  #this will save the Pytest execution output in test_output.txt
