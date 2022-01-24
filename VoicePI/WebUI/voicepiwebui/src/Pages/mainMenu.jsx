import { Button, Paper, Typography } from "@material-ui/core";
import AccessibilityIcon from '@mui/icons-material/Accessibility';
import ImageIcon from '@mui/icons-material/Image';
import KeyboardIcon from '@mui/icons-material/Keyboard';
import LanguageIcon from '@mui/icons-material/Language';
import * as React from 'react';
import { useState } from 'react';
import { useNavigate } from 'react-router';
import "./mainMenu.css";



const MainMenu = () => {
    const [loading, setloading] = useState(true);



    const divst = {height:"100%", width:"100%"};

    const iconStyle = {transform: "scale(2.0)"};

    const navigate = useNavigate();


    
    

    

    const [fetchdata, setFetchData] = useState(null);

    if(loading===true){
    fetch(`http://192.168.207.86:5000/wetter`)
            .then((response) => response.json())
            .then((data) =>setFetchData(data))
            .then((data)=>console.log(fetchdata))
            .then((data)=>setloading(false))
            .catch((err)=>console.log(err));
        }

    return(
        <>
        {!loading && <div class="wrapper">
            <div style={{position: 'fixed', top: 0, left: 0}}>
                {
                    //ip + ':) ... ' + fetchdata.wetter
                }
            </div>
          
            <div class="one">
                <Paper style={divst}>
                    <Button onClick={()=>{navigate("/webbrowser");}} startIcon={<LanguageIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} > <Typography variant='h5'>Webbrowser</Typography> </Button>
                </Paper>
            </div>
            
            <div class="two">
                <Paper style={divst}>
                    <Button onClick={() => navigate("/image")} startIcon={<ImageIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} > <Typography variant='h5'>ImageDisplay</Typography></Button>
                </Paper>
            </div>

            <div class="six">
                <Paper style={divst}>
                    <Button onClick={() => navigate("/silentmode")} startIcon={<KeyboardIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}}><Typography variant='h5'>SilentMode</Typography></Button>
                </Paper>
            </div>
            
            <div class="four">
                <Paper style={divst}>
                    <Button onClick={()=>{}} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h5'>Video/Audio</Typography></Button>
                </Paper>
            </div>
            
            <div class="five">
                <Paper style={divst}>
                    <Button onClick={()=>{}} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h5'>Wetter</Typography></Button>
                </Paper>
            </div>
            
            <div class="sus">
                <Paper style={divst}>
                    <Button onClick={() => navigate("/help")} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h5'>Help</Typography></Button>
                </Paper>
            </div>
        </div> }
        </>
    );
};

export default MainMenu;