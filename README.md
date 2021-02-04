# coffee_machine
Implementation of a coffee machine

This application has been written in Python. On Ubuntu, python can be installed with

```
sudo apt update
sudo apt-get install python3.6
```

To run the file, in the terminal run 

```
python3 app.py
```

Then enter the name of the input JSON file (input_1.json contains tje example case) containing the initial configuration and ingredients.

The app will create a coffee machine from the config file and run it through different scenarios.

Unit testing has been done using the pytest framework.

If pytest is not installed, it can be installed by 

```
pip3 install pytest
pip3 install pytest-cov
```

A test coverage report has been generated. You can seen the results in test_coerage.png





