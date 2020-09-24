
var questions = [{
    question : " 7+5",
    choices:["2","3","4","12"],
    correctanswer:3 },
    {
        question : " 9+5",
    choices:["2","3","4","14"],
    correctanswer:3 },
    {
        question : " 12+5",
    choices:["12","33","17","16"],
    correctanswer:2 },
    {
        question : " 17+5",
    choices:["22","20","23","21"],
    correctanswer:0 },
    {
        question : " 14+5",
    choices:["12","19","15","18"],
    correctanswer:1 }];
var currentquestion = 0;
var correctanswer = 0;
var quizover = false;


$(document).ready(function(){
    displaycurrentquestion();
    $(this).find(".quizmessage").hide();
    $(this).find(".nextbutton").on("click",function(){
        console.log(quizover+"QZ")
        if(!quizover) {
           var value = $("input[type='radio']:checked").val();
            console.log(value);
            if (value == undefined) {
                $(document).find(".quizmessage").text("Please select an answer");
                $(document).find(".quizmessage").show();
                
            }
            else {
                $(document).find(".quizmessage").hide();
                if(value == questions[currentquestion].correctanswer)
                    { correctanswer++; console.log("Correct"); }
                currentquestion++;
                if(currentquestion<questions.length){ displaycurrentquestion(); }  
                else{ displayscore();
                    $(document).find(".nextbutton").text("play again?");
                    quizover = true;
                     console.log("quizover1")
                    }
                
                
            }
        } else {
            quizover = false;
            console.log("quizover2")
            $(document).find(".nextbutton").text("Next Question");
            resetquiz();
            displaycurrentquestion();
            hidescore();
        }
        
    });
                  
    

function displaycurrentquestion() {
    console.log("In display current question");
    var question = questions[currentquestion].question;
    var questionclass = $(document).find(".quizContainer > .question");
    var choicelist = $(document).find(".quizContainer > .choicelist"); 
    var numchoices = questions[currentquestion].choices.length;
    
    $(questionclass).text(question);
    $(choicelist).find("li").remove();
    
    
    var choice;
   
    for ( i=0; i < numchoices; i++){
        choice = questions[currentquestion].choices[i];
        $('<li><input type="radio" value =' +i+ '>'+ choice +'</li>').appendTo(choicelist);
        
    }
                             
    
}

function resetquiz() {
    currentquestion = 0;
    correctanswer = 0;
    hidescore();
    console.log("resetted")
}
function displayscore(){
    $(document).find(".quizContainer > .result").text("You scored:"+ correctanswer+"out of:" + questions.length )
    $(document).find(".quizContainer > .result").show();
    
}
function hidescore() {
    $(document).find(".result").hide();
    console.log('hidded')
}

});
