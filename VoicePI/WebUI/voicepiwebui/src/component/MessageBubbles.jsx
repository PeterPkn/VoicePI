import React from "react";
import { Paper, Typography } from "@material-ui/core";

import './TypingAnimCss.css'



export default function MessageBubble({message, alignLeft}){

    let sender = 'VoicePI:';
    let isTyping = false;
    console.log(message);
    if(message === "VoicePI: ..."){
        isTyping = true;
    }

    let typingStyle = {
        
    };

    const Typing = () => (
        <div className="typing">
          <div className="typing__dot"></div>
          <div className="typing__dot"></div>
          <div className="typing__dot"></div>
        </div>
      );

    if(message.startsWith('YOU:')){
        sender = 'YOU:';
        message = message.replace('YOU:', '');
    }else{
        message = message.replace('VoicePI:', '');
    }


    let style = {margin:10, alignSelf:'end', textAlign:'end', background:'lightgreen'};

    if(alignLeft){
        style = {margin:10, alignSelf:'start', background:'lightblue'};
    }

    return(
        <Paper elevation={7} style={style}>
            {isTyping && <Typing />}

            {!isTyping && <><Typography style={{alignSelf:'start'}} variant="subtitle2">{sender}</Typography>
            <Typography style={{padding:10, wordWrap: "break-word"}}>{message}</Typography></>}
            </Paper>

    );

}