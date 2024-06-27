let Usertxt = document.getElementById("Usertxt")
let Chattxt = document.getElementById("Chattxt")
let ChatBox = document.getElementById("ChatBox")
let btn = document.getElementById("btn")

btn = addEventListener("click",()=>{
    User = Usertxt.innerHTML = ChatBox.value;
    Chatting();
})

function Chatting(){
    if (User = "Hi, My name is Sagnik Dey") {
        return Chattxt.innerHTML = "Hi how can I help you?"
    }
}
