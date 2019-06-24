const formdata = {};

function register(formE1) {

    for (let control of formE1) {
        formdata[control.id] = control.value;
    }
    console.log('Data', formE1, formdata);
    formE1.reset();

    sessionStorage.setItem('userData', JSON.stringify(formdata));
    // window.location ="hero.html";



    const req = new XMLHttpRequest();
    req.onload = () => {
        console.log('Response: ', req.responseText);

    };

    const safeData = {};

    for(let k in formdata) {
        if(k) {
            safeData[k] = formdata[k];
        }
    }

    req.open('POST', 'https://us-central1-qac-sandbox.cloudfunctions.net/setUser');
    req.setRequestHeader('Content-Type', 'application/json');
    req.send(JSON.stringify(safeData));

    return false;
}

