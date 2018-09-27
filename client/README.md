# client

## First off
Working with front end frameworks can take some getting used to. It can get overwhelming at first, so if you've got a question or don't understand something, don't hesitate to post in the frontend slack channel and someone will get back to you.

## Front End Stuff
**HTML** - HyperText Markup Language is used to create the basic structure and content of a webpage.

**CSS** - Cascading Style Sheets are used for the design of a webpage – where everything is placed and how it looks.

**JavaScript** - Used to define the interactive elements of a webpage that help to engage users.

**JavaScript frameworks** - An analogy that is often used to help explain the concept of JavaScript frameworks to new developers is to think of building a website like building a house. When you begin to build a house, you could create all of your own building materials from scratch and start building without any blueprints, but that approach would be very time-consuming.
The more sensible approach would be to buy pre-manufactured building materials, such as wood and bricks, and then assemble them based on a blueprint to fit your specific needs. Coding a website is very similar. When you begin, you could code every aspect of the site from scratch, but there are common website features that make more sense to apply from a template. If you need a wheel, for instance, it’s a lot more sensible to
￼buy one than it is to reinvent it. And that’s where frameworks come into play.

**Vue** - https://vuejs.org/

### Quick Note
We will use Vue's Single-File Component layout, which means that the HTML, CSS and JavaScript for a component is all in a single .vue file.
---

## Tutorials & Helpful References
- [Google](https://www.google.ca/) - The most helpful of them all.
- [HTML Basics](https://www.w3schools.com/html/html_basic.asp) - The whole HTML5 Tutorial there is a great resource when looking stuff up.
- [CSS Tutorials](https://www.w3schools.com/Css/) - W3Schools is always helpful.
- [Flexbox Froggy](https://flexboxfroggy.com/) - Game for learning CSS Flexbox.
- [Vue Docs](https://vuejs.org/v2/guide/) - Official Vue Documentation
---

## Code Editors
I use Atom, others use Sublime, I know of some guy who uses VS Code. Use whatever you want, they can all be configured with different plugins and packages to help with web development. Highly recommend that you set up syntax highlighting for .vue files with whichever editor you choose though.
---

## Project setup
You can run these commands once you cd into this (client) directory on your local repository.

### Install dependencies
*Make sure you have npm installed*
https://www.npmjs.com/get-npm
Run this command the first time you pull down this repo to install all the apps dependencies. If you add a new dependency to the project, please mention it on your pull request and in the frontend channel so that people will know to reinstall their local dependencies. If someone else adds a new dependency and mentions it on the slack channel, once their changes make it to the main branch and you pull the changes down, you will have to re-run this command to install the new dependency.
```
npm install
```

### Compiles and hot-reloads for development
*This is the one you will use the most*
Run this command after you have installed the apps dependencies. Running this command will start up your local development server. Once the the dev server is running, it will tell you that the app is running at http://localhost:8080/. Type this address into a web browser and you're app should load up. While your local web server is running, you can make changes to your code (be sure to save the changed files) and the app will automatically be reloaded with those changes.
```
npm run serve
```

### Compiles and minifies for production
*Only run this when we're actually going to deploy with backend*
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
