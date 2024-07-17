let Usertxt = document.getElementById("Usertxt")
let Chattxt = document.getElementById("Chattxt")
let ChatBox = document.getElementById("ChatBox")
let btn = document.getElementById("btn")

btn = addEventListener("click",()=>{
    User = Usertxt.innerHTML = ChatBox.value;
    Chatting();
})

function Chatting(){
    if (User == "Hi, My name is Sagnik Dey") {
        return Chattxt.innerHTML = "Hi how can I help you?"
    }
    else if (User == "How are you?"){
        return Chattxt.innerHTML = "I am fine"
    }
    else if (User == "What is the Capital of India?"){
        return Chattxt.innerHTML = "Delhi"
    }
    else if (User == "What is your Name?"){
        return Chattxt.innerHTML = "My name is ChatBot"
    }
    else if (User == ""){
        return Chattxt.innerHTML = ""
    }
    else {
        return Chattxt.innerHTML = "Didn't get that"
    }

}
