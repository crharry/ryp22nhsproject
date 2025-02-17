// Import
const { HTMLToJSON } = require('html-to-json-parser'); // CommonJS
const fs = require('node:fs');

const { argv } = require('node:process');
//argv[0]= nodejs location |argv[1]= node program location |argv[2]= file to read 



//input HTML(file)
var html = "<test>File Not Found By Node Program</test>";
if (argv.length > 2){
    html = fs.readFileSync(argv[2],"utf8");
}





function removewhitespacefromstart(html) {
  if(!html) return html;
  

  //https://www.textfixer.com/tutorials/javascript-line-breaks.php
  html = html.replace(/(\r\n|\n|\r|\t)/gm, "");
  //console.log(html);
  //remove (some single tag elements, non unicode chararcters, comments)
  html = html.replace(/<!(?!-?>)(?!.*--!>)(?!.*<!--(?!>)).*?(?<!<!-)>/gm, "");
  //console.log(html);
  html = html.replace(/(<br>|<hr>)/gm, "");
  //html = html.replace(/(<html.*>)/gm, "<html>");
  //html = html.replace(/(<script.*script>)/gm, "");
  html = html.replace(/(<c-wiz.*c-wiz>)/gm, "");
  //console.log(html);
  return html.replace(/^\s+|\s+$/gm, "");

}



html = removewhitespacefromstart(html);

//htmlformatting sync function
const waitforhtmlformatting = new Promise((resolve, reject) => {
  resolve(html);
});

//HTML to JSon




waitforhtmlformatting.then((html) => {
  //console.log(html);
  const element = html; // HTML string
  //console.log(element);
  result = HTMLToJSON(element,true); // Default: false - true: return JSON, false: return JS Object
  waitforjson();
});




//output
async function waitforjson(){
    let jsonOutput = new Promise(function(resolve,reject){
        resolve(result);
    });
    result = await jsonOutput;
    console.log(result);
}


//console.log(result);
