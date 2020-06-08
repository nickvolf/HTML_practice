var quizContainer = document.getElementById('quiz-root');

function shuffle(arra1) {
    var ctr = arra1.length, temp, index;
// While there are elements in the array
    while (ctr > 0) {
// Pick a random index
        index = Math.floor(Math.random() * ctr);
// Decrease ctr by 1
        ctr--;
// And swap the last element with it
        temp = arra1[ctr];
        arra1[ctr] = arra1[index];
        arra1[index] = temp;
    }
    return arra1;
}

function removeItem(arr, value){
  var index = arr.indexOf(value);
  if (index > -1){
    arr.splice(index, 1);
  }
  return arr;
}

function generateQuiz(){
  // First mix the order of the cwquestions
  var mixCWQuestions = shuffle(cwquestions);
  var mixCSQuestions = shuffle(csquestions);
  var mixPNQuestions = shuffle(pnquestions);
  var mixRPQuestions = shuffle(rpquestions);
  var question_type = "";


  function displayCWQuestion(cwQuestion){
    question_type = "cwQuestion"
    var imageContainer = document.getElementById('cw-image-container');
    var questionContainer = document.getElementById('cw-sentence-container');
    var mixChoice = shuffle(cwQuestion.answers)
    var selectMenuHTML =  '<select name="" id="choices"><option id="cw-option-1" value="1">' +mixChoice[0]+' </option><option id="cw-option-2 "value="2">' +mixChoice[1]+' </option><option id="cw-option-3" value="3">' +mixChoice[2]+' </option><option id="cw-option-4 "value="4">' +mixChoice[3]+' </option></select>'

    imageContainer.src = cwQuestion.image;
    questionContainer.innerHTML = "<h5>" + cwQuestion.sentenceTextPre + " " + selectMenuHTML + " " + cwQuestion.sentenceTextPost + "</h5>";
  }

  function displayCSQuestion(csQuestion){
    question_type = "csQuestion"
    var imageContainer = document.getElementById('cw-image-container');
    var questionContainer = document.getElementById('cw-sentence-container');
    var mixChoice = shuffle(csQuestion.answers)
    var selectMenuHTML =  '<select name="" id="choices"><option id="cw-option-1" value="1">' +mixChoice[0]+' </option><option id="cw-option-2 "value="2">' +mixChoice[1]+' </option><option id="cw-option-3" value="3">' +mixChoice[2]+' </option><option id="cw-option-4 "value="4">' +mixChoice[3]+' </option></select>'

    imageContainer.src = csQuestion.image;
    questionContainer.innerHTML = "<h5>" +  selectMenuHTML + "</h5>";
  }

  function displayPNQuestion(pnQuestion){
    question_type = "pnQuestion"
    var imageContainer = document.getElementById('cw-image-container');
    var questionContainer = document.getElementById('cw-sentence-container');
    var mixChoice = shuffle(pnQuestion.answers)
    var selectMenuHTML =  '<select name="" id="choices"><option id="cw-option-1" value="1">' +mixChoice[0]+' </option><option id="cw-option-2 "value="2">' +mixChoice[1]+' </option></select>'

    imageContainer.src = pnQuestion.image;
    questionContainer.innerHTML = "<h5>" +  selectMenuHTML + "</h5>";
  }

  function displayRPQuestion(rpQuestion){
    question_type = "rpQuestion"
    var imageContainer = document.getElementById('cw-image-container');
    var questionContainer = document.getElementById('cw-sentence-container');
    var mixChoice = shuffle(rpQuestion.answers)
    var selectMenuHTML =  '<select name="" id="choices"><option id="cw-option-1" value="1">' +mixChoice[0]+' </option><option id="cw-option-2 "value="2">' +mixChoice[1]+' </option></select>'

    imageContainer.src = rpQuestion.image;
    questionContainer.innerHTML = "<h5>" + rpQuestion.asked + "<br />" + selectMenuHTML + "</h5>";
  }

  function checkCWAnswer(cwQuestion) {
    var correctAnswer = cwQuestion.correctAnswer;
    var answerContainer = document.getElementById('choices');
    var userAnswer = answerContainer.options[answerContainer.selectedIndex].text;

    if (userAnswer===correctAnswer){
      console.log('Check cw Great Job, Keep Going!');
      cwQuestion.numCorrect++;
      quizScore = quizScore + cwQuestion.points;
      if(cwQuestion.numCorrect >= 2 ){
        mixCWQuestions = removeItem(mixCWQuestions, cwQuestion);
      }
    }
    else{
      cwQuestion.numCorrect--;
      console.log(cwQuestion.numCorrect)
    }
  }

  function checkCSAnswer(csQuestion) {
    var correctAnswer = csQuestion.correctAnswer;
    var answerContainer = document.getElementById('choices');
    var userAnswer = answerContainer.options[answerContainer.selectedIndex].text;

    if (userAnswer===correctAnswer){
      console.log('Check CS Great Job, Keep Going!');
      csQuestion.numCorrect++;
      quizScore = quizScore + csQuestion.points;
      if(csQuestion.numCorrect >= 2 ){
        mixCSQuestions = removeItem(mixCSQuestions, csQuestion);
      }
    }
    else{
      csQuestion.numCorrect--;
      console.log(csQuestion.numCorrect)
    }
  }

  function checkPNAnswer(pnQuestion) {
    var correctAnswer = pnQuestion.correctAnswer;
    var answerContainer = document.getElementById('choices');
    var userAnswer = answerContainer.options[answerContainer.selectedIndex].text;

    if (userAnswer===correctAnswer){
      console.log('Check PN Great Job, Keep Going!');
      pnQuestion.numCorrect++;
      quizScore = quizScore + pnQuestion.points;
      if(pnQuestion.numCorrect >= 2 ){
        mixPNQuestions = removeItem(mixPNQuestions, pnQuestion);
      }
    }
    else{
      pnQuestion.numCorrect--;
      console.log(pnQuestion.numCorrect)
    }
  }

  function checkRPAnswer(rpQuestion) {
    var correctAnswer = rpQuestion.correctAnswer;
    var answerContainer = document.getElementById('choices');
    var userAnswer = answerContainer.options[answerContainer.selectedIndex].text;
    console.log("Correct Answer: " + correctAnswer + "User Answer: " + userAnswer)
    if (userAnswer===correctAnswer){
      console.log('Check RP, Great Job, Keep Going!');
      rpQuestion.numCorrect++;
      quizScore = quizScore + rpQuestion.points;
      if(rpQuestion.numCorrect >= 2 ){
        mixRPQuestions = removeItem(mixRPQuestions, rpQuestion);
      }
    }
    else{
      rpQuestion.numCorrect--;
      console.log(rpQuestion.numCorrect)
    }
  }

  displayCWQuestion(mixCWQuestions[0]);


  submitButton.onclick = function () {
    if(question_type==="cwQuestion"){
      checkCWAnswer(mixCWQuestions[0]);

      if (mixCWQuestions.length > 0){
        mixCWQuestions = shuffle(mixCWQuestions);
        displayCWQuestion(mixCWQuestions[0]);


      }else if(mixCSQuestions.length > 0){
        displayCSQuestion(mixCSQuestions[0]);


      }else if(mixPNQuestions.length > 0){
        displayPNQuestion(mixPNQuestions[0]);


      }else if(mixRPQuestions.length > 0){
        displayRPQuestion(mixRPQuestions[0]);


      }else{
        alert("All Done!")
      }
    }

    else if(question_type==="csQuestion"){
      checkCSAnswer(mixCSQuestions[0]);

      if(mixCSQuestions.length > 0){
        mixCSQuestions = shuffle(mixCSQuestions);
        displayCSQuestion(mixCSQuestions[0]);


      }else if(mixPNQuestions.length > 0){
        displayPNQuestion(mixPNQuestions[0]);


      }else if(mixRPQuestions.length > 0){
        displayRPQuestion(mixRPQuestions[0]);


      }else{
        alert("All Done!")
      }
    }

    else if(question_type==="pnQuestion"){
      checkPNAnswer(mixPNQuestions[0]);

      if(mixPNQuestions.length > 0){
        mixPNQuestions = shuffle(mixPNQuestions);
        displayPNQuestion(mixPNQuestions[0]);


      }else if(mixRPQuestions.length > 0){
        displayRPQuestion(mixRPQuestions[0]);


      }else{
        alert("All Done!")
      }
    }

    else if (question_type==="rpQuestion"){
      checkRPAnswer(mixRPQuestions[0])
        if (mixRPQuestions.length > 0){
          mixRPQuestions = shuffle(mixRPQuestions)
          displayRPQuestion(mixRPQuestions[0])

        } else {
          alert('Finished! ' + quizScore + " points gained!")
        }
      }
      else {
        alert("Finished! " + quizScore + " points gained!")
      }
    }
  }


var submitButton = document.getElementById('submit-button')
generateQuiz();
