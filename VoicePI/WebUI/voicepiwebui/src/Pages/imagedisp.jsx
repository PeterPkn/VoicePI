import * as React from 'react';
import { useState } from 'react';
import { Typography, Button, Divider, Box, MobileStepper, Paper } from "@material-ui/core";
import KeyboardArrowLeft from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import SwipeableViews from 'react-swipeable-views';
import { autoPlay } from 'react-swipeable-views-utils';
import ImageIcon from '@mui/icons-material/Image';
import { useNavigate } from 'react-router';
import { useTheme } from '@material-ui/core';



const AutoPlaySwipeableViews = autoPlay(SwipeableViews);

const images = [
  {
    label: 'Image 1',
    imgPath:
      'https://via.placeholder.com/400x400?text=Hello!',
  },
  {
    label: 'Image 2',
    imgPath:
    'https://via.placeholder.com/400x400?text=Hello!',  },
  {
    label: 'Image 3',
    imgPath:
    'https://via.placeholder.com/400x400?text=Hello!',  },
  {
    label: 'Image 4',
    imgPath:
    'https://via.placeholder.com/400x400?text=Hello!',  },
];

function SwipeableTextMobileStepper() {
  const theme = useTheme();
  const [activeStep, setActiveStep] = React.useState(0);
  const maxSteps = images.length;

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleStepChange = (step) => {
    setActiveStep(step);
  };

  return (
    <Box sx={{ maxWidth: 400, flexGrow: 1 }}>
      <Paper
        square
        elevation={0}
        sx={{
          display: 'flex',
          alignItems: 'center',
          height: 50,
          pl: 2,
          bgcolor: 'background.default',
        }}
      >
        <Typography>{images[activeStep].label}</Typography>
      </Paper>
      <AutoPlaySwipeableViews
        axis={theme.direction === 'rtl' ? 'x-reverse' : 'x'}
        index={activeStep}
        onChangeIndex={handleStepChange}
        enableMouseEvents
      >
        {images.map((step, index) => (
          <div key={step.label}>
            {Math.abs(activeStep - index) <= 2 ? (
              <Box
                component="img"
                sx={{
                  height: 255,
                  display: 'block',
                  maxWidth: 400,
                  overflow: 'hidden',
                  width: '100%',
                }}
                src={step.imgPath}
                alt={step.label}
              />
            ) : null}
          </div>
        ))}
      </AutoPlaySwipeableViews>
      <MobileStepper
        steps={maxSteps}
        position="static"
        activeStep={activeStep}
        nextButton={
          <Button
            size="small"
            onClick={handleNext}
            disabled={activeStep === maxSteps - 1}
          >
            Next
            {theme.direction === 'rtl' ? (
              <KeyboardArrowLeft />
            ) : (
              <KeyboardArrowRight />
            )}
          </Button>
        }
        backButton={
          <Button size="small" onClick={handleBack} disabled={activeStep === 0}>
            {theme.direction === 'rtl' ? (
              <KeyboardArrowRight />
            ) : (
              <KeyboardArrowLeft />
            )}
            Back
          </Button>
        }
      />
    </Box>
  );
}

function ImageDisp(){

    const iconStyle = {transform: "scale(1.5)", padding:"1%"};
    const navigate = useNavigate();


    return(
        <div style={{width:"100%", height:"90vh"}}>
            <div style={{display:"flex"}}>
                <Button onClick={()=>{navigate('/')}} style={{minWidth:'100px', minHeight:'50px'}}>Back</Button>
                <ImageIcon style={iconStyle}/>
                <Typography variant='h4'>
                    Image
                </Typography>
            </div>
            <Divider></Divider>
            <SwipeableTextMobileStepper style={{}}></SwipeableTextMobileStepper>
            
        </div>

    );
}


export default ImageDisp;