// var cardHeader=document.querySelector(".card-header");
// var cardBody=document.querySelector(".card-body");

// var openClose=true;
// cardHeader.addEventListener("click",function(){
//     if(openClose){
//         cardBody.style.visibility = "hidden"
//         openClose=false
//     }else{
//         cardBody.style.display="block"
//         openClose=true
//     }
// })

var btn=document.querySelector(".btnRight");
var box=document.querySelector(".box");
var poss=0;
btn.addEventListener("click",function(){
    box.style.left=poss+"px"
    poss+=20;
    
})

var btn=document.querySelector(".btnLeft");
var box=document.querySelector(".box");
var poss=0;
btn.addEventListener("click",function(){
    box.style.left=poss+"px"
    poss-=20;
    
    var btn=document.querySelector(".btnLeft");
    var box=document.querySelector(".box");
    var poss=0;
    btn.addEventListener("click",function(){
        box.style.left=poss+"px"
        poss-=1000;
        
    })