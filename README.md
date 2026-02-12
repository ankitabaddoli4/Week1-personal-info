## Personal Information Manager

## Project Overview

Personal Information Manager is my first Python project.
The objective of this project is to learn basic Python programming concepts such as variables, user input, output formatting, calculations, and simple error handling.

This project demonstrates how personal information can be stored, processed, and displayed using Python.

## Project Description

This is a beginner-friendly Python program that stores and displays personal information.
Some information is stored directly in the program, while other details are collected from the user during execution.

The program validates user input, performs a simple calculation, and presents all information in a well-formatted output.

## Project Goals and Objectives

Learn Python syntax and structure
Understand how variables and data types work
Practice taking input from users

## What I Learned
 Variables

Learned how to store different types of data such as strings and integers.

Input / Output

Used input() to collect user information and print() to display results.

String Formatting

Used f-strings to create clean and readable output.

 Error Handling

Implemented basic validation using while loops to avoid empty input.

 Calculations

Calculated age in months from age in years using arithmetic operations.

## Features

Stores static information:

Name

Age

City

Hobby

Gets dynamic information from the user:

Favorite food

Favorite color

Email address

Country

Displays all information in a formatted layout

Uses basic input validation

Calculates age in months

## How to Run This Program
Prerequisites

Python must be installed on your system

Steps

Open Terminal / Command Prompt

Navigate to the project folder:

cd Week1-Personal-Info


Run the program:

python personal_info.py


Follow the prompts and enter your details

## Sample Output
==================================================
        PERSONAL INFORMATION MANAGER
==================================================

Please tell me about yourself:
----------------------------------------
What's your favorite food? Pizza
What's your favorite color? Blue
What's your email address? riya@gmail.com
Which country are you from? India

==================================================
              YOUR INFORMATION
==================================================

Name           : Riya
Age            : 21 years (252 months old)
City           : Pune
Hobby          : Reading books

Favorite Food  : Pizza
Favorite Color : Blue
Email          : riya@gmail.com
Country        : India

==================================================
Thank you for using the program!
==================================================

## Challenges & Solutions
Challenge 1: User enters empty input

Solution:
Used while loops to repeatedly ask for input until valid data is entered.

Challenge 2: Formatting output neatly

Solution:
Used f-strings and spacing to align text properly.

## Technical Details
Algorithms Used

Sequential execution

Input validation using loops

Arithmetic calculation for age conversion

Data Structures

Variables (strings and integers)

Program Architecture

Single Python file

Clear sections:

Welcome message

Static data

User input

Calculation

Output display

## Testing Evidence
Test Case	Input	Result
Normal input	Pizza, Blue	Program runs correctly


No crashes for valid input

Prevents empty values

## Code Structure
Week1-Personal-Info/
│── personal_info.py
│── README.md
│── test_inputs.txt
└── .gitignore

## Visual Documentation

Screenshots should include:

Running program in terminal

User input prompts

Final output display

Project folder structure


## Quality Standards Checklist

 Clear project overview and objectives
 Step-by-step setup instructions
 Well-organized file structure
 Explanation of logic and calculations
 Input validation and testing
 Visual proof (screenshots)








