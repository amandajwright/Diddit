$(document).ready(function() {


$('#datepicker').datepicker({
            uiLibrary: 'bootstrap4'
        });
});

function createNode(element) {
  return document.createElement(element);
}
function append(parent, element) {
  return parent.appendChild(element);
}

const ul = document.getElementByID("all_tasks");
const url = 'http://127.0.0.1:5000/v1/entries/tasks/all'

fetch(url)
  .then((resp) => resp.json())
  .then(function(data) {
    let tasks = data.results;
    return tasks.map
  })
  .catch(function(error) {

  })

//https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data

//
// $.each( response, function( line ) {//loop through lines in response
//     var keys = [];
//     var values = [];
//     $.each( line, function( obj ) {
//         keys.push( Object.keys(obj) );//get keys
//         for( var key in obj ) {
//             values.push(obj[key]);//get values
//         }
//     });
//     lines.push({ {'keys':keys},{'values':values} });
// });
