
function openModalWindow() {
  let modalWindow = document.getElementsByClassName("modalContainer")[0];
  modalWindow.style.display = "block";
}
function closeModalWindow() {
  let modalWindow = document.getElementsByClassName("modalContainer")[0];
  modalWindow.style.display = "none";
}


/* quiz code:
  - each page will have 8 questions
  - only one will show at a time
  - back/next buttons allow user to cycle through the questions
  - at the end, javascript creates a submit and submit button
  - this submit will send the data to flask which will store it in scores table using sql

  - the page will pass a json string to js with questions and answers upon loading.
*/
let currScore = 0;
let currQuestion = 0; // currQuestion == 8 => go to submit/submit
let jsonQuestions = "";
var questions; // contains list of question elements on page
var submit; // submit for the end of quiz
function loadQuiz(jsonString) {
  currScore = 0;
  currQuestion = 0;
  jsonQuestions = jsonString;
  questions = document.getElementsByClassName("question");
  submit = document.getElementsByClassName("submitSlide")[0];
}

function cycleQuestion(change) {
  // accepts integer -1/+1 for back/next

  if (currQuestion + change > 0 && currQuestion < 9) {
    if(currQuestion < 8) {
      questions[currQuestion].style.display = "none";
      questions[currQuestion + change].style.display = "block";
    } else {
      questions[currQuestion].style.display = "none";
      submit.style.display = "block";
    }
  }

}
