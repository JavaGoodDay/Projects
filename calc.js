

function calc() {
    const num1 = +document.getElementById('inputA').value;
    const num2 = +document.getElementById('inputB').value;

    return {
        add: function add() {
            result = (num1 + num2);
             document.getElementById('resultpane').innerText = result;
        },
    

        multiply: function multiply() {
            result = (num1 * num2);
             document.getElementById('resultpane').innerText = result;
        },
    

        subtract: function subtract() {
            result = (num1 - num2);
             document.getElementById('resultpane').innerText = result;
        },
    

        divide: function divide() {
            result = (num1 / num2);
             document.getElementById('resultpane').innerText = result;
        },
    }
}