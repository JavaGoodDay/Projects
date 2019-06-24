const animals = ['elephant','tiger','zebra','dog','cat','emu'];

const output = animals 
    .filter(item => item.length == 3) 
    .reduce((prev, item) => prev+=''+item+', ','Animals: ')
    .slice(0,-2);
   
;