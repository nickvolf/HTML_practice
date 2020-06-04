var myQuestions = [
  {
    question: "What is 10/2",
    answers: {
      a: '3',
      b: '5',
      c: '100'
    },
    correctAnswer: 'b'
  },
  {
    question: "How hot",
    answers: {
      a: 'Like fire',
      b: 'Not hot',
      c: 'A bit'
    },
    correctAnswer: 'a'
  }
];

function generateQuiz(questions, quizContainer, resultsContainer, submitButton){

  //Function to create the html on the page
  function showQuestions(questions, quizContainer){

    //we'll need a place to store the output and the answers choices
    var output = [];
    var answers;

    for (var i=0;i < questions.length;i++){
      //first reset the list of answers
      answers = [];

      //for each available answer to the question...
      for(letter in questions[i].answers){
        // ...add an html radio button
        answers.push(
          '<label class="form-check-label mb-2">'
            + '<input class="ml-1" type="radio" name="question'+i+'" value="'+letter+'">'
            + letter + ': '
            + questions[i].answers[letter]
          + '</label>'
        );
      }

      // add this question and its answers to the output
      output.push(
        '<div class="question mb-2">' + questions[i].question + '</div>'
        + '<div class="answers">' + answers.join('') + '</div>'
      );
    }

    // finally combine our output list into one string of html and put it on the page
    quizContainer.innerHTML = output.join('');
  }


  //Show the results of the quiz after submit is clicked
	function showResults(questions, quizContainer, resultsContainer){
		// gather the answer containers from our quiz_name
    var answerContainers = quizContainer.querySelectorAll('.answers');

    //keep track of the users answerContainers
    var answer = '';
    var numCorrect = 0;

    //for each question...
    for(var i = 0; i < questions.length; i++){

      // find the seleceted answer
      userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;

      // if answer is correctAnswer
      if(userAnswer===questions[i].correctAnswer){
        numCorrect++;
        answerContainers[i].style.color = 'lightgreen';
      }
      else{
        answerContainers[i].style.color = 'red';
      }
    }

    resultsContainer.innerHTML = numCorrect + ' out of ' + questions.length;
	}

	// show the questions
	showQuestions(questions, quizContainer);

	// when user clicks submit, show results
	submitButton.onclick = function(){
		showResults(questions, quizContainer, resultsContainer);
	}
}

var quizContainer = document.getElementById('quiz');
var resultsContainer = document.getElementById('results');
var submitButton = document.getElementById('submit');

generateQuiz(myQuestions, quizContainer, resultsContainer, submitButton);
