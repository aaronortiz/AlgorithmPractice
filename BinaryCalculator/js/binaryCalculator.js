function displayAddCharacter(character) {

  res = document.getElementById("res");

  if (res) {
    res.innerHTML += character;
  }

}

function handleDigit(digit) {

  var allowedDigits = /^(0|1){1}$/g;

  if (allowedDigits.test(0)) {
    displayAddCharacter(digit);
  } else {
    console.log("digit " + digit + " failed test " + allowedDigits.source);
  }

}

function handleClr() {

  res = document.getElementById("res");

  if (res) {
    res.innerHTML = "";
  }

}

function handleEql() {

  isValidOperation = /^(0|1)+(\+|\-|\*|\/)(0|1)+$/

  res = document.getElementById("res");

  if (res && isValidOperation.test(res.innerHTML)) {
    res.innerHTML = getResultString(res.innerHTML);
  } else {
    console.log("Invalid operation: " + res.innerHTML);
  }

}

function handleOp(operator) {

  res = document.getElementById("res");

  if (res) {
    const allowedOps = /^(\+|\-|\*|\/){1}$/;
    const opAlreadyExists = /\+|\-|\*|\//;

    if (allowedOps.test(operator)) {
      if (opAlreadyExists.test(res.innerHTML)) {
        console.log("Operator already exists in " + res.innerHTML);
      } else if (res.innerHTML.length == 0) {
        console.log("Operator cannot be first character.");
      } else {
        displayAddCharacter(operator);
      }

    } else {
      console.log("Operator " + operator + " not allowed.");
    }
  }
}

function getResultString(operation) {

  const isOperator = /(\+|\-|\*|\/)+/;
  result = 0;
  // Split operands and operators
  operationParts = operation.split(isOperator);
  var leftOperand = (parseInt(operationParts[0], 2));
  const rightOperand = (parseInt(operationParts[2], 2));

  switch (operationParts[1]) {
    case "+":
      result = leftOperand + rightOperand;
      break;
    case "-":
      result = leftOperand - rightOperand;
      break;
    case "*":
      result = leftOperand * rightOperand;
      break;
    case "/":
      result = Math.floor(leftOperand / rightOperand);
      break;
    default:
      console.log("Smoke test failed: ... operator not recognized: " + operationParts[1]);
  }

  return result.toString(2);

}