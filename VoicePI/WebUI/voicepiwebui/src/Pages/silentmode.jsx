import * as React from 'react';
import { useState, useRef } from 'react';
import { Typography, Button, Divider, TextField, IconButton } from "@material-ui/core";
import KeyboardIcon from '@mui/icons-material/Keyboard';
import SendIcon from '@mui/icons-material/Send';
import { useNavigate } from 'react-router';
import MessageBubble from '../component/MessageBubbles';


export default function SilentMode(){

    const inputRef = useRef();
    const iconStyle = {transform: "scale(1.5)", padding:"1%"};
    const navigate = useNavigate();
    const [messages, setmessages] = useState([]);

    function sendMessage(){
        if(inputRef.current.value !== ''){
            setmessages(['VoicePI: ' + '...', 'YOU: ' + inputRef.current.value, ...messages]);
            

            fetch(`http://192.168.207.86:5000/silentmode`, {
                method: "POST",
                body: JSON.stringify({
                    msg: inputRef.current.value,
                }),
            })
                .then((response) => response.text())
                .then((data) => {
                    console.log(data)
                    setmessages(['VoicePI: ' + data.answ, 'YOU: ' + inputRef.current.value, ...messages]);
                })
                .then(()=>inputRef.current.value = '')
                .catch((error) => {
                    console.error(error);
                });


        }
    }

    return(

        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <Button onClick={()=>{navigate('/')}} style={{minWidth:'100px', minHeight:'50px'}}>Zurück</Button>
                <KeyboardIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Silent Mode
                </Typography>
            </div>
            <Divider></Divider>

            <div style={{maxHeight:'75vh', overflow:'auto', display:'flex', flexDirection:'column-reverse'}}>
            {messages.map(message=>{
                if(message.startsWith('YOU:')){
                    return <MessageBubble message={message} alignLeft={false} />;
                }
                return <MessageBubble message={message} alignLeft={true} />;
            })}  
            </div>

            <div style={{width:'95%', display:'flex', flexDirection:'row', margin:'20px', position:'absolute', bottom: 0}}>
                <TextField onKeyUp={(code)=>{if(code.code === 'Enter'){sendMessage();}}} inputRef={inputRef} label='Type your message here.' variant='outlined' style={{flexGrow:'1'}} ></TextField> <IconButton onClick={sendMessage}><SendIcon/></IconButton>
            </div>
        </div>

    );
}