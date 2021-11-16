import * as React from 'react';
import { useState } from 'react';
import { Typography, Button, Paper, Box } from "@material-ui/core";
import LanguageIcon  from '@mui/icons-material/Language';


function Webbrowser(){


    const iconStyle = {transform: "scale(1.5)", padding:"1%"};


    return(
        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <LanguageIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Webbrowser
                </Typography>
            </div>
            <iframe style={{width:"100%", height:"100%"}} src="https://www.google.com/webhp?igu=1"></iframe>

        </div>
    );
}

export default Webbrowser;