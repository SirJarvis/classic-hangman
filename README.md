# Classic Hangman
Hangman is a Python terminal game, which runs in the Code Institue mock terminal on Heroku.

Players try to guess the letters of the hidden word before they ran out of lives.

![responsive.png](documentation/images/responsive.png)

---

## How to play

Classic hangman is very intuitive and fun game. In this game user will easily start a game by just typing first letter. If user guesses a letter that's in the word it will display in terminal on the line, if user doesn't guess a word terminal will show a head of hangman as a first sign of wrong letter guessing. At the end of the game user can choose to play again or not.

---



## UX User Experience

**User Goals**
* As a user i want to have fun with game.
* As a user i want the game to be challenging.

**User Stories**

**As a user, I want the game to be intuitive.**
* The user should be able to understand easy game steps by just typing guessing letters.

**As a user, I want to quickly start the game.**
* The user should be able to see message "Guess a hidden letter or word:" and easily start the game.

**As a user, I would like to be able to choose if i want to play a new game or not.**
* The user should be able to see at the end of game option Play Again? (Y/N).


**Project Goal**

* The main goal of this project is to make minimum design game that will be easy, simple and quick to play for all age groups.
---

## Features

**Existing features**

* Welcome screen
* Accept user inputs

![feature1.png](documentation/images/feature1.png)

* Shows when user didn't guess letter

![feature2.png](documentation/images/feature2.png)

* Shows when user already guessed same letter

![feature3.png](documentation/images/feature3.png)

* Game shows to user new parts of hangman each time user doesn't guess a letter

![feature4.png](documentation/images/feature4.png)

* In case the user lost, game will show actual hidden word, wish user "Good luck next time and it will offer user with option to play game again

![feature5.png](documentation/images/feature5.png)

---

**Future Features**

* Different levels of difficulty
* Add scoring system
* Add option for player name input

---

## Technologies Used

**Languages used**
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

**Programs used**
* [GitHub](https://github.com/) Github was used to store the project.
* [GitPod](https://www.gitpod.io/) GitPod was used for writing code.
* [Heroku](https://www.heroku.com/) Heroku was used to deploy project.
* [PEP8online](http://pep8online.com/) PEP8online Validator was used to check for errors in code.

**Libraries**
* random was used to select a random word.

---
## Testing

* Code has been tested through [PEP8](http://pep8online.com/)
* The Website was successfuly tested on [ResponsiveDesign](http://ami.responsivedesign.is/#)
* Manually tested user inputs by inputing incorrect data to confirm error messages were capturing wrong inputs.

**Validator Testing**

**1 error was returned when passing through the** [PEP8online](http://pep8online.com/)

![pep8.png](documentation/images/pep8.png)

**On second testing trough the** [PEP8online](http://pep8online.com/) No errors were shown after i fixed error on line 40 "line to long".

![pep8correct.png](documentation/images/pep8correct.png)

---

---

## Fixed errors
**I was able to resolve:** 
* Trailing whitespace error
* Expected an intented block(comment)
* Continuation line unaligned for hanging indent
* line to long [66,80]
* Line to long [48,80]
* Line to long [40,80]
---
![problem2.png](documentation/images/problem2.png)

---
![problem3.png](documentation/images/problem3.png)

---
![problem4.png](documentation/images/problem4.png)


---
![problem.png](documentation/images/problem.png)


---
![problem5.png](documentation/images/problem5.png)



---
---
## Deployment

**The project was deployed using Code Institutes mock terminal for Heroku**

**Deployment steps:**
* Fork or clone this repository
* requirements.txt can be left empty as this project does not use any external libraries
* Create a new app in [Heroku](https://www.heroku.com/)
* Select "New" and "Create new app"
* In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list)
* While still in "Settings", click "Reveal Config Vars" and input the following. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
* Click on "Deploy" and select your deploy method and repository
* Click "Connect" on selected repository
* Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section
* Heroku will now deploy the site

---

## Credits

**Code**
* [MDN](https://developer.mozilla.org/en-US/), [W3SCHOOLS](https://www.w3schools.com/), [STACKOVERFLOW](https://stackoverflow.com/), [TRAVERSY MEDIA](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA), [FREECODECAMP](https://www.youtube.com/c/Freecodecamp/videos), [PYTHONTUTOR](https://pythontutor.com/visualize.html#mode=edit),
[DEV.TO](https://dev.to/), [KITE](https://www.youtube.com/c/KiteHQ/videos)

   For me this was a part of new coding experience and this project was additional learning processs, with enormous help of all mentioned resources above that were used on daily basis, i was able to better understand and write the code and it's structure. I used tutorial lesson as a learning process for creating while loop, adding visual stages to hangman, and creating functions from [KITE](https://www.youtube.com/c/KiteHQ/videos).

* This readme document was based on research on several readme documents such as the Code Institute's readme [Sample](https://github.com/Code-Institute-Solutions/SampleREADME).

* I used the lessons learned during the Code Institute "Love Sandwiches" project to better understand the code.


**Acknowledgements**

* My partner, for her time, patience, effort and infinite support.
* My mentor, Chris Quinn, for all valuable sessions, all advices and guidance.
* Code Institute and Slack community for their help and support at any time.