let locations= new Array();
let numOfLocations=0;

function add(){
    let temp="";
    
    var location=document.getElementById('loc').value;
    
    locations.push(location);
    numOfLocations++;

    
    for (let i=0; i<numOfLocations; i++){
        temp=temp+"\n"+locations[i];
        document.getElementById('selLoc').value=temp;
    }
    
    document.getElementById('loc').value= "";
    }

function passLocations(){
    locations=document.getElementById('selLoc').value;
    return locations
}
function getInfo(){
    temp= String( document.getElementById('temp').value);
    rain= String(document.getElementById('rain').value);
    snow= String(document.getElementById('snow').value);
    wind=  String(document.getElementById('wind').value);
    date= String(document.getElementById('date').value);

    let info=new Array();
    info =[temp, rain, snow, wind, date];
    return info
   
}


