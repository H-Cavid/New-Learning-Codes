// var obj={
//     name:"Cavid",
//     surname:"Hesenov"

// }
// //console.log(typeof obj)
// //constructor function
// function Human(_name,_surname,_age){
//     this.name=_name;
//     this.surname=_surname;
//     this.age=_age
// }
// var Yeni_obyekt=new Human("Cavid","Hesenov",18);

// class Animal{
//     constructor(_type,_color){
//         this.type=_type;
//         this.color=_color;
//     }
//     getFullInfo(){
//         return this.type+ "-" +this.color
//     }
// }
// var anim=new Animal("Etyeyen","Qirmizi")
var submitBtn=document.getElementsByTagName("button")[0];
var FirstNameInput=document.getElementsByTagName("input")[0]
var LastNameInput=document.getElementsByTagName("input")[1]
var EmailInput=document.getElementsByTagName("input")[2]
var PasswordInput=document.getElementsByTagName("input")[3]
var DateInput=document.getElementsByTagName("input")[4]
var MaleInput=document.getElementsByTagName("input")[5]
var FemaleInput=document.getElementsByTagName("input")[6]
var PhoneNumberInput=document.getElementsByTagName("input")[7]
//addEventListener('starter event',event function')

submitBtn.addEventListener("click",function(){
    var txt="Sizin Adiniz:"+FirstNameInput.value+"Sizin Soyadiniz:"+LastNameInput.value+"Sizin Email addresiniz:"+EmailInput.value+"Sizin parolunuz"+PasswordInput.value+"Sizin dogum tarixiniz:"+DateInput.value+"Sizin cinsiniz:"+MaleInput.value+"Sizin cinsiniz:"+FemaleInput.value+"Sizin telefon nomreniz:"+PhoneNumberInput.value;
    console.log(txt)
})