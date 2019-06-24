

const userdata = JSON.parse(sessionStorage.getItem('userData'));

const namespan = document.getElementById('namespan');

namespan.innerText = userdata['First Name'] + ' ' + userdata['Last Name'];

function NavReg() {
    window.location = 'reg.html';
}