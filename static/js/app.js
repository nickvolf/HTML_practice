// Examine the document object //

// console.dir(document);
// console.log(document.domain);
// console.log(document.url);
// console.log(document.title);
// console.log(document.doctype);
// console.log(document.head);
// console.log(document.body);
// console.log(document.all);
// console.log(document.forms);
// console.log(document.links);
// console.log(document.images);

///////////////
// Selectors //
//////////////

////////////////////////
// GET getElementById //
////////////////////////

// console.log(document.getElementById("header-title"));
// var headerTitle = document.getElementById('header-title');
// var header = document.getElementById('main-header');
// console.log(headerTitle);
// headerTitle.textContent = 'Show hidden Style'
// headerTitle.innerText = "Doesn't show hidden style"
// headerTitle.innerHTML = '<h3>Add element into the DOM object</h3>'
// header.style.borderBottom = 'solid 3px #000';

// getElementsByClassName //
// var items = document.getElementsByClassName('list-group-item');
// items[1].textContent = 'Hello 2';
// items[1].style.fontWeight = 'bold';
// items[1].style.backgroundColor = 'yellow';

// for (var i=0; i < items.length;i++){
//   items[i].style.backgroundColor = '#f4f4f4';
// }

///////////////////////////
// GET ELEMENTSBYTAGNAME //
///////////////////////////

// var li = document.getElementsByTagName('li');
// li[1].textContent = 'Hello 2';
// li[1].style.fontWeight = 'bold';
// li[1].style.backgroundColor = 'yellow';

/////////////////////
// Query Selectors //
/////////////////////

// //Get By Id with #
// var header = document.querySelector('#main-header');
// header.style.borderBottom = 'solid 4px #ccc';
//
// //Get by Element
// var input = document.querySelector('input');
// input.value = "Hello world";
//
// var submit = document.querySelector(('input[type="submit"]'));
// submit.value = "Send";
//
// //Get by class us a .
// var item = document.querySelector('.list-group-item');
// item.style.color = 'red';
//
// var lastItem = document.querySelector('.list-group-item:last-child');
// lastItem.style.color = 'blue';
//
// var secondItem = document = document.querySelector('.list-group-item:nth-child(2)');
// secondItem.style.color = 'coral';
//
// var titles = document.querySelectorAll('.title');
// console.log(titles);
//
// var odd = document.querySelectorAll('li:nth-child(odd)');
// var even = document.querySelectorAll('li:nth-child(even)');
// for (var i=0; i < odd.length; i++){
//   odd[i].style.backgroundColor = "#f4f4f4";
//   even[i].style.backgroundColor = "#ccc";
// }

var userName = document.getElementById("prof-banner-username")
console.log(userName)
