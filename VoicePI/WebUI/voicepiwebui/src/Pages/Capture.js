import * as React from 'react';
import { useState, useRef } from 'react';
import { Typography, Button, Divider, TextField, IconButton } from "@material-ui/core";
import KeyboardIcon from '@mui/icons-material/Keyboard';
import SendIcon from '@mui/icons-material/Send';
import { useNavigate } from 'react-router';
import MessageBubble from '../component/MessageBubbles';


export default function Capture(){

    const inputRef = useRef();
    const iconStyle = {transform: "scale(1.5)", padding:"1%"};
    const navigate = useNavigate();
    const [messages, setmessages] = useState([]);

    function take_photo(){

        fetch(`http://192.168.207.86:5000/silentmode`, {
                method: "POST",
                body: JSON.stringify({
                    msg: "photo",
                }),
            }).catch((error) => {
                    console.error(error);
                });


    }

    function take_video(){

        fetch(`http://192.168.207.86:5000/silentmode`, {
                method: "POST",
                body: JSON.stringify({
                    msg: "video",
                }),
            }).catch((error) => {
                    console.error(error);
                });


    }

    return(

        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <Button onClick={()=>{navigate('/')}} style={{minWidth:'100px', minHeight:'50px'}}>Zurück</Button>
                <KeyboardIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Photo / Video Mode
                </Typography>
            </div>
            <Divider></Divider>

            <div style={{display:"flex", height:'90vh', justifyContent:"space-around", alignItems: "center"}}>
            <Button variant='outlined' style={{width:'30vw', height: '30vh'}} onClick={take_video} >Video</Button>
            <Button variant='outlined' style={{width:'30vw', height: '30vh'}} onClick={take_photo} >Photo</Button>
            </div>
        </div>

    );
}