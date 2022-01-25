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
    const [loading, setloading] = useState(false);



    const divst = {height:"100%", width:"100%"};

    const iconStyle = {transform: "scale(2.0)"};

    const navigate = useNavigate();


    
    

    

    const [fetchdata, setFetchData] = useState(null);

    function listen_call(){
        fetch(`http://192.168.207.86:5000/silentmode`, {
                method: "POST",
                body: JSON.stringify({
                    msg: 'listen',
                }),
            }).catch((error) => {
                    console.error(error);
                });
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
                    <Button onClick={listen_call} startIcon={<LanguageIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} > <Typography variant='h5'>Listen</Typography> </Button>
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
                    <Button onClick={()=>navigate("/capture")} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h5'>Video/Foto</Typography></Button>
                </Paper>
            </div>
            
            <div class="five">
                <Paper style={divst}>
                    <Button onClick={()=>navigate("/wetter")} startIcon={<AccessibilityIcon sx={iconStyle}/>} style={{height:"100%", width:"100%"}} ><Typography variant='h5'>Wetter</Typography></Button>
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