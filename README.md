# Mend_Interview
Code test for Mend in Orlando, FL.

Note: These instructions are for MacOS. The terminal commands may need to be editted slightly for a Windows machine.

Setup the environment:

I wrote these tests using the latest release of Python 2.7 and Selenium Webdriver. If you do not have these installed, please follow the instructions in the links below. You will need the Selenium server (section 1.5 of the Selenium tutorial). <br>
Python: https://www.python.org/downloads/<br>
Selenium: http://selenium-python.readthedocs.io/installation.html

You will also need to have JDK installed on your machine. You can download it here:<br>
http://www.oracle.com/technetwork/java/javase/downloads/jdk10-downloads-4416644.html

Lastly, you will need to have Chrome installed. You can dowload it here:<br>
https://www.google.com/chrome/?brand=CHBD&gclid=EAIaIQobChMIr6vh482u2gIVTS-BCh233grAEAAYASAAEgKXuvD_BwE&gclsrc=aw.ds&dclid=CNCwjObNrtoCFc2_ZAodc4YJiA

Download (or clone) the files from this repository to an easily accessible folder on your machine.

Running the tests:

1. Start the Selenium server by running the Selenium server jar file you downloaded earlier.

<pre>java -jar selenium-server-standalone-2.x.x.jar</pre>

If these are not in your PATH, use this command:
<pre>/path/to/java -jar /path/to/selenium-server-standalone-2.x.x.jar</pre>

2. Navigate in your terminal to the test files.

3. Run the first test.

<pre>python test1.py</pre>

This test should open a Chrome web browser, navigate to codecademy.com, and then throw an error that the items were not found.

4. Run the next test.

<pre>python test2.py</pre>

This test should open a Chrome web browser, navigate to codecademy.com, and successfully log in and out.
