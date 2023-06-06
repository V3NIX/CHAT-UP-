# CHAT-UP!
Chat-UP!
Chat-UP! is a secure chat application using Python and the TKinter library. It uses an SQLite database to store data and socket programming to transmit messages over a network. User authentication is handled using OpenLDAP and socket layer security is provided through the use of x509 certificates.

Getting Started
To use Chat-UP!, follow the instructions below.

*Prerequisites*
Python 3.x installed on your system.
SQLiteStudio installed on your system.
*Running the Application*
1.Start the server by running the server.py file.
2.Run the main_interface.py file to open the main interface of Chat-UP!.
3.In the main interface, you can register a new user by clicking on the "Register" button. Fill in the required information in the registration form and submit it.
4.After registering, you can log in by clicking on the "Login" button. Enter your username and password in the login form and click on the "Login" button.
5.Once logged in, you will be able to see the list of connected users in the chat application.
6.Select a user from the list and click on the "Chat" button to start a conversation with that user.
7.In the chat window, type your message in the input box at the bottom and click on the "Send" button to send the message to the selected user.
8.The message will be displayed in the chat window, and you can continue the conversation by sending more messages.
*Files*
The Chat-UP! application consists of the following files:

-main_interface.py: This file contains the code for the main interface of the chat application.
-login.py: This file contains the code for the login form.
-reg.py: This file contains the code for the registration form.
-client.py: This file contains the code for the client-side of the chat application.
-server.py: This file contains the code for the server-side of the chat application.
-user.db : This file contains the database of the registred users.
Note: Make sure to run the server.py file before running the other files to ensure proper communication between the client and server.

*Dependencies*
=OpenSSL: a python package that provides a high-level interface to the functions in the OpenSSL library such as X509 certs generation
=Tkinter: Standard Python interface to the Tk GUI toolkit.
=SQLiteStudio: desktop application for browsing and editing SQLite database files.
![image](https://github.com/V3NIX/CHAT-UP-/assets/117733151/f78a64ca-4f6a-4a26-82f7-8b1a3b604c67)
