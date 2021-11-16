import * as React from 'react';
import { useState } from 'react';
import "./mainMenu.css";
import { Typography, Button, Paper } from "@material-ui/core";
import LanguageIcon  from '@mui/icons-material/Language';
import KeyboardIcon from '@mui/icons-material/Keyboard';
import ImageIcon from '@mui/icons-material/Image';
import AccessibilityIcon from '@mui/icons-material/Accessibility';
import { useNavigate } from 'react-router';


const MainMenu = () => {
    const [State, setState] = useState(null);

    const divst = {height:"100%", width:"100%"};

    const iconStyle = {transform: "scale(2.0)"};

    const navigate = useNavigate();

    let amogus = new Audio("https://srv4.onlymp3.net/download?file=8c61c2c8e24482eea2e2f8baef1863d0251003003&token=pm_iGsxePy1Wxc9WQ8L2xw&expires=1636486376148&s=rKgv3KeW3f6NjV3LtPXlqA");

    const playmogus = () => {
        amogus.play();
    };

    return(
        <div class="wrapper">
          
            <div class="one">
                <Paper style={divst}>
                    <Button onClick={()=>{navigate("/webbrowser");}} startIcon={<LanguageIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} > <Typography variant='h4'>Webbrowser</Typography> </Button>
                </Paper>
            </div>
            
            <div class="two">
                <Paper style={divst}>
                    <Button startIcon={<ImageIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} > <Typography variant='h4'>ImageDisplay</Typography></Button>
                </Paper>
            </div>

            <div class="six">
                <Paper style={divst}>
                    <Button startIcon={<KeyboardIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}}><Typography variant='h4'>Silent Voice Mode</Typography></Button>
                </Paper>
            </div>
            
            <div class="four">
                <Paper style={divst}>
                    <Button onClick={playmogus} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h4'>SUS</Typography></Button>
                </Paper>
            </div>
            
            <div class="five">
                <Paper style={divst}>
                    <Button onClick={playmogus} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h4'>SUS</Typography></Button>
                </Paper>
            </div>
            
            <div class="sus">
                <Paper style={divst}>
                    <Button onClick={playmogus} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h4'>SUS</Typography></Button>
                </Paper>
            </div>
        </div>
    );
};

export default MainMenu;