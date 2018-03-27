
#### 1. Steps for running Nightwatch along with Selenium server for E2E (EndtoEnd) Funcitonal Browser Testing
```
$ java -version   # check to makesure JAVA is installed on the machine
$ brew install node  # if node is not installed install it

# this will install all node modules specified in package.json file (in our case chromedriver, selenium, )
# and it's dependencies in the current directory where the below command ran
$ npm install     

# this will run the task named 'nightwatch' under scripts in package.json file, task name can be any name
$ npm run nightwatch   
```

See below Nightwatch Page Objects & Commonds, that is where real fun of Nightwatch is (see file1, file2 )
______________________________________________________________________________________________________________________
#### 2. Best articls on Testing from internet 

1. An Overview of [JavaScript Testing in 2018](https://medium.com/welldone-software/an-overview-of-javascript-testing-in-2018-f68950900bc3)
+ as per Author (highlighted on page) : TL;DR; Use Jest for unit & integration tests, TestCafe for UI tests
 

2. The easy way to start [automatically testing website : NightWatch](https://medium.freecodecamp.org/how-to-easily-start-automatically-testing-your-website-8629ea8df04a)
+ details on installaiton of Java, Selenium, webdriver, nightwatch and configuration



3. UI Testing with [Nightwatch.js – Page Objects](http://matthewroach.me/ui-testing-with-nightwatch-js-page-objects/)
+ These 2 files takes care of login page testing in modular way with PageObjects and Commands [file1](https://github.com/matthewroach/nightwatch-demo/blob/master/page-objects/commandsLogin.js) and  [file2](https://github.com/matthewroach/nightwatch-demo/blob/master/tests/login-command-object.js)


4. E2E [Testing TodoMVC](https://blog.cloudboost.io/e2e-testing-with-nightwatch-part-two-aaa25a4dc033)
+ practical way to test a funcitonal website, has github repo
