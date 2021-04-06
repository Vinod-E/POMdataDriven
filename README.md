# POM

**_STEP - 1_**

Create page Objects -- Under pageObject package -> Pages directory

    **Note:** Maintain unique pages objects

**_STEP - 2_**

Create Test case file -- Under Scripts -> module directory, for pages objects 
and call the functions which are required to test case file

    **Note:** Maintain separte folder for each module. To better experience to debuging and understandable

**_STEP - 3_**

Create Test Suite file -- Under testSuite package, To run all the scenarios which are included 
in scripts folder.

Folder wise explanation
-----------------------
## Config

**config** - It has every server URL's and parse the same under utilities package to use 
while run the script

**ConfigFile** - It has the OS support path variables

**Environment** - This contains launching browser and closing browser class function. 
And it will ask tester some inputs(server, sprint) for script run.

**inputFile** - It has the OS support path variables

**outputFile** - It has the OS support path variables

## Listeners

**logger_settings** - It capture all failure logs

**screenShot** - When ever web element failed by any reason it captures the screenshot

## utilities

Under this package having all common selenium functionalities are we using in scripts development.
just import and call them.