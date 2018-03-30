This project was bootstrapped with [Create React App](https://github.com/facebookincubator/create-react-app).

### 1. Install React boilerplate app as follows
```
npx create-react-app my-app
cd my-app
npm start

```
$ npm start  will open a web page http://localhost:3000/ ,  source code is in /src/App.js and the Class in it is a Component not ReactComponent .


### 2. Install Jest & test it
 + [from jest site](https://facebook.github.io/jest/docs/en/getting-started.html)
 + $ node install jest --save-dev
 + As mentioned on the web page add  sum.js  & sum.test.js files
 + Add the following section to your package.json: ( replace whatever you had under "scripts" )
 + run $ npm test
```
{
  "scripts": {
    "test": "jest"
  }
}
```

### 3. Install Enzyme and other dependencies as below [as stated in this blog](https://medium.com/@mateuszsokola/configuring-react-16-jest-enzyme-typescript-7122e1a1e6e8)

+ $ npm i --save-dev enzyme enzyme-adapter-react-16 jest react-test-renderer

### 4. Configuring Jest + Enzyme
  + setup.js — to setup enzyme to use React 16.
  + shim.js — to get rid of warnings regarding missing browser polyfills.
  + create both these files under a dir 'config' ( can be any name)


https://stackoverflow.com/questions/47781736/jest-cannot-find-module-setupdevtools-from-setup-js

```
npm install --save-dev babel-jest
npm install --save-dev babel-preset-env


create  .babelrc file as follws

{
  "presets": [
     "react",
     "es2015"
  ]
}


"jest"  in package.json is as follows

 "jest": {
    "setupFiles": [
      "<rootDir>/config/shim.js",
      "<rootDir>/config/setup.js"
    ],
    "transform": {
      "^.+\\.jsx?$": "babel-jest"
    }
  }
```

### 5. Here is Working final package.json ,
  + have file like this , and issue command $ npm install , so it will update all dependencies
  + /src/Foo.js /src/__tests__/Foo.test.js  files are created
  + $npm test
  + $ npm test -- --watch    // this will watch dir and run in auto mode when files changes 

```
{
  "name": "my-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "babel-preset-env": "^1.6.1",
    "enzyme-adapter-react-16": "^1.1.1",
    "enzyme-to-json": "^3.3.3",
    "i": "^0.3.6",
    "react": "^16.2.0",
    "react-dom": "^16.2.0",
    "react-scripts": "1.1.1",
    "react-test-renderer": "^16.3.0"
  },
  "scripts": {
    "test": "jest"
  },
  "jest": {
    "setupFiles": [
      "<rootDir>/config/shim.js",
      "<rootDir>/config/setup.js"
    ],
    "transform": {
      "^.+\\.jsx?$": "babel-jest"
    }
  },
  "devDependencies": {
    "babel-jest": "^22.4.3",
    "babel-polyfill": "^6.26.0",
    "babel-preset-es2015": "^6.24.1",
    "babel-preset-react": "^6.24.1",
    "enzyme": "^3.3.0",
    "jest": "^22.4.3",
    "react-addons-test-utils": "^15.6.2"
  }
}
```



