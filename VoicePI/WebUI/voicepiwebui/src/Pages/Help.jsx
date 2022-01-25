import * as React from 'react';
import { Typography, Button, Paper, Divider } from "@material-ui/core";
import AccessibilityIcon from '@mui/icons-material/Accessibility';
import { useNavigate } from 'react-router';


function Help() {

    const iconStyle = {transform: "scale(1.5)", padding:"1%"};
    const navigate = useNavigate();


    return(
        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <Button onClick={()=>{navigate('/')}} style={{minWidth:'100px', minHeight:'50px'}}>Zurück</Button>
                <AccessibilityIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Help
                </Typography>
            </div>
            <Divider></Divider>
            <Paper elevation={7} style={{margin:'30px'}}>
                <Typography style={{margin:'10px'}} variant='h5'>Was macht Silent Mode?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} Der Silent Mode lässt dich per Text mit dem VoicePI kommunizieren.</Typography>
            </Paper>

            <Paper elevation={7} style={{margin:'30px'}}>
                <Typography style={{margin:'10px'}} variant='h5'>Wie Spreche ich mit dem VoicePI?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} Die Talk Taste auf dem MainMenu drücken und den Befehl sagen.</Typography>
            </Paper>

            <Paper elevation={7} style={{margin:'30px'}}>
                <Typography style={{margin:'10px'}} variant='h5'>Wie mache ich ein Foto?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} Im Hauptmenü die FOto Option wählen.</Typography>
            </Paper>
        </div>
    );
}

export default Help;