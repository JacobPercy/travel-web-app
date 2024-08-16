// Array of questions, each with a question, options, and correct answer
let questions = [
    {
      question: "Question 1",
      options: ["These", "Are", "Placeholders", "Thanks"],
      correct: "A"
    },
    {
      question: "Question 2",
      options: ["These", "Are", "Placeholders", "Thanks"],
      correct: "C"
    },
    {
      question: "Question 3",
      options: ["These", "Are", "Placeholders", "Thanks"],
      correct: "A"
    },
  ];

  let currentQuestion = 0;
  let score = 0;

  document.getElementById("question-text").textContent = questions[currentQuestion].question;
  let optionsHTML = "";
  questions[currentQuestion].options.forEach((option, index) => {
    optionsHTML += `<li><input type="radio" name="answer" value="${String.fromCharCode(65 + index)}"> ${option}</li>`;
  });
  document.getElementById("options").innerHTML = optionsHTML;

  document.getElementById("next-button").addEventListener("click", () => {
    let userAnswer = document.querySelector("input[name='answer']:checked").value;

    if (userAnswer === questions[currentQuestion].correct) {
      score++;
    }

    currentQuestion++;

    if (currentQuestion >= questions.length) {
      document.getElementById("score-text").textContent = `Score: ${score}/${questions.length} (${Math.round((score / questions.length) * 100)}%)`;
      document.getElementById("next-button").disabled = true;
    } else {
      document.getElementById("question-text").textContent = questions[currentQuestion].question;
      optionsHTML = "";
      questions[currentQuestion].options.forEach((option, index) => {
        optionsHTML += `<li><input type="radio" name="answer" value="${String.fromCharCode(65 + index)}"> ${option}</li>`;
      });
      document.getElementById("options").innerHTML = optionsHTML;
    }
  });