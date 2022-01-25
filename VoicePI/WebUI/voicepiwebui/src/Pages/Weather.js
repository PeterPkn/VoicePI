import * as React from 'react';
import { useState, useRef } from 'react';
import { Typography, Button, Divider, TextField, IconButton } from "@material-ui/core";
import KeyboardIcon from '@mui/icons-material/Keyboard';
import SendIcon from '@mui/icons-material/Send';
import { useNavigate } from 'react-router';
import MessageBubble from '../component/MessageBubbles';


export default function Weather(){

    const inputRef = useRef();
    const iconStyle = {transform: "scale(1.5)", padding:"1%"};
    const navigate = useNavigate();
    const [locweather, setlocweather] = useState([]);

    function weather(){
        fetch('http://192.168.207.86:5000/wetter')
            .then(response => response.json())
            .then(data => setlocweather(data));
    }

    return(

        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <Button onClick={()=>{navigate('/')}} style={{minWidth:'100px', minHeight:'50px'}}>Zurück</Button>
                <KeyboardIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Wetter
                </Typography>
                <Typography>{locweather["temperature"]}</Typography>
            </div>


            <Divider></Divider>

            
        </div>

    );
}