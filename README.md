## Windows
1-install virtualenv.
2- activate the environment. (.\ENVVIRONMENT NAME\Scripts\activate)
3- install dependencies:
    pip install -r requirements.txt
4- do some filters:
    python image_filter input output logo filter1 filter2 ...
    example:
    python image_filter input.jpg output.jpg python.png 50 overlay gray_scale 180 overlay

## Linux
to activate the environment:
source env/bin/activate
to do some filters:
python3 image_filter input output logo filter1 filter2 ...
example:
python3 image_filter input.jpg output.jpg python.png 50 overlay gray_scale 180 overlay


to test the code:
pytest test.py

the output of test in the terminal, then the html report will be displayed automatically in browser.



#I spend about 5 hours to finish the task
