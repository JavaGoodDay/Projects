// const request = new XMLHttpRequest();
// request.onload = function(){
//    console.log(request.responseText);
//    console.log('loaded!');
// };


// console.log('sent!');

const imageMap = {
    'Molecule Man' : 'antman.jpeg',
    'Madame Uppercut' : 'cpmarvel.jpeg',
    'Eternal Flame' : 'humtorch.jpeg'
};


function fetchSuperheroes() {
    const request = new XMLHttpRequest();

    request.onload = () => {
        const parsedData = JSON.parse(request.responseText);
        console.log('DATA:', parsedData);
        // displaySuperheroData(parsed);
 
        document.getElementById('homeTown').innerText = parsedData.homeTown;
        document.getElementById('formed').innerText = parsedData.formed;
        document.getElementById('secretBase').innerText = parsedData.secretBase;

        for(let member of parsedData.members) {

            const memberContainer = document.createElement('div')

            const el = document.createElement('h3');
            el.innerText = member.name;
            memberContainer.append(el);

            for(let power of member.powers){
                
            const abilities = document.createElement('p1');
            abilities.innerText = power + (' ');
            memberContainer.append(abilities);

            }

            const age = document.createElement('p');
            age.innerText = ("age: " + member.age);
            memberContainer.append(age);
            
            const identity = document.createElement('p');
            identity.innerText = ("Secret Identity: " + member.secretIdentity);
            memberContainer.append(identity);

            const image = document.createElement('img');
            image.src = imageMap[member.name];
            memberContainer.append(image);

        
            

            document.getElementById('members').append(memberContainer)


            // document.getElementById('members').innerText += member.name + ' ';
        }
       
    };
request.open('GET',  'https://raw.githubusercontent.com/ewomackQA/JSONDataRepo/master/example.json');

request.send();

}


fetchSuperheroes();