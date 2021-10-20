import * as React from 'react';
import { useState } from 'react';
import { Grid, Typography, Button } from "@material-ui/core";

const MainMenu = () => {
    const [State, setState] = useState(null);


    return(
        <Grid container spacing={{ xs: 2, md: 2 }} columns={{ xs: 12, sm: 6, md: 12 }}>
        <Grid item xs={12} sm={6}>
            <Button>
                <Typography>
                    SUS
                </Typography>
            </Button>
        </Grid>
        
        <Grid item xs={12} sm={6}>
            <Button>
                <Typography>
                    SUS
                </Typography>
            </Button>
        </Grid>

        <Grid item xs={12} sm={6}>
            <Button>
                <Typography>
                    SUS
                </Typography>
            </Button>
        </Grid>

        <Grid item xs={12} sm={6}>
            <Button>
                <Typography>
                    SUS
                </Typography>
            </Button>
        </Grid>

    </Grid>
    );
};

export default MainMenu;