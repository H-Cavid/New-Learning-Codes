var removeBtn=document.querySelector(".input-group-text");
var addBtn=document.querySelector("input[type='button']")
var form=document.querySelector("form")
function removeElement(elem){
elem.parentElement.parentElement.removeChild(elem.parentElement)
}
var frmData=form.innerHTML
addBtn.addEventListener("click",function(){  
 frmData+=`
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="Name Surname">
                    <div class="input-group-append" onclick="removeElement(this)">
                        <span class="input-group-text">
                            Remove
                        </span>
                    </div>
                </div>
 `


})

form.innerHTML=frmData