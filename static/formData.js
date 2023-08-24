let locations= new Array();
let numOfLocations=0;

function add(){
   
    
    var location=document.getElementById('loc').value;
    
    locations.push(location);
    numOfLocations++;

    let temp=locations[0]
    
    for (let i=1; i<numOfLocations; i++){
        temp=temp+"\n"+locations[i];  
    }
   
    document.getElementById('selLoc').value=temp;
    document.getElementById('loc').value= "";
    }

function clearLoc(){

    numOfLocations=0;
    while (locations.length > 0) {
        locations.pop();
      }
      document.getElementById('selLoc').value="";
}



