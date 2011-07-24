# django-PedanticLogging

This piece of middleware for django will save the HTML outputted in debug mode to a specified directory, even in a production environment!  This piece of middleware was created in conjunction with the development of CouchConnect.com

## System Requirements
This has been designed and tested on Django 1.2, but should be compatible with both 1.1 and 1.3.

## Installation
Drop it into your project and add its path to your middleware tuple, then set

    PEDANTIC_LOG_DIR = "/absolute/path/to/logs/"

Note the trailing slash and that the directory you specify should be permission 666

    sudo chmod 666 /absolute/path/to/logs/

## Feedback
It's welcome, I may have overlooked something.  Get at me on twitter [@nuckin42](http://twitter.com/nuckin42)