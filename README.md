# Scoring System
## An assignment for intermediate coding class.

### Demo

[![Scoring system demo](https://img.youtube.com/vi/BQAyotParqM/0.jpg)](https://youtube.com/shorts/BQAyotParqM?feature=share)

### Assignment
Project Name: Scoring System

Project Structure:

    Judge : id, name, introduction
    
    Team : id, name, members
    
    Mark : id, judge, team, task type (1 - performance, 2 - presentation ), date time, points
    
    Game : add_mark(), get_marks()
    
    Screen: show panel: help, score, judges, teams, marks

    CommandCenter : 
      1. initial judges, teams. 
      2. show screens and accept commands

Tasks:

1. Work on the panel of all judges with their name and introduction
2. Work on the panel of all teams with their name and members
3. Work on the panel of all marks with all information required
4. Work on the panel of scoreboard which should show the rank correctly
5. Update the help panel to show the usage of each command
6. Load data to initialize judges, teams and marks
7. Save data to data files 
/data/judges.txt
/data/teams.txt
/data/marks.txt