
# Student–Job Skill Analysis System

A beginner-friendly Python project that compares student
skills with job requirements and reports matching skills,
missing skills, and the match percentage.

## Technologies
- Python
- Object-Oriented Programming
- Core Python libraries only

## Requirements
- Python 3.8 or newer
- No external packages
- No database required

## How to Run

Open a terminal in the project folder and run:

    python main.py

## Project Files
- main.py: Starts the application and runs tests.
- models.py: Stores student and job information.
- analyzers.py: Compares skills and calculates the score.
- manager.py: Coordinates analysis and displays the report.

## Match Formula

Match Percentage =
(Matching Skills / Total Required Skills) * 100

If there are no required skills, the score is defined as 0%.

## OOP Concepts
- Classes and objects
- Encapsulation
- Inheritance
- Abstraction
- Polymorphism
- Method overriding

## Limitations

The system uses exact skill-name matching. It does not
measure skill proficiency, experience, or hiring probability.