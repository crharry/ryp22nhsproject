// Import
const { HTMLToJSON } = require('html-to-json-parser'); // CommonJS
const fs = require('node:fs');




//input (HTML(file for now) --> URL)
var html = "<test></test>";
html = fs.readFileSync("file2.html","utf8");


//https://www.textfixer.com/tutorials/javascript-line-breaks.php
html = html.replace(/(\r\n|\n|\r)/gm, "");
//console.log(html);


//HTML to JSon
const element = html; // HTML string
let result = HTMLToJSON(element,true); // Default: false - true: return JSON, false: return JS Object


//output
async function waitforjson(){
    let jsonOutput = new Promise(function(resolve,reject){
        resolve(result);
    });
    result = await jsonOutput;
    console.log(result);
}

waitforjson();
//console.log(result);