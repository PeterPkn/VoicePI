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
                <Typography style={{margin:'10px'}} variant='h5'>Wie mache ich das?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} So macht man das!</Typography>
            </Paper>

            <Paper elevation={7} style={{margin:'30px'}}>
                <Typography style={{margin:'10px'}} variant='h5'>Wie mache ich das nummer 2?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} So macht man das nummer 2!</Typography>
            </Paper>

            <Paper elevation={7} style={{margin:'30px'}}>
                <Typography style={{margin:'10px'}} variant='h5'>Sind das gute Fragen?</Typography>
                <Typography  style={{margin:'10px'}}variant='h6'>{'\t'} Ja, sicher!</Typography>
            </Paper>
        </div>
    );
}

export default Help;