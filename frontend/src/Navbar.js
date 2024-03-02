import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

const navItems = [];

export default function Navbar() {
  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar>
        <Toolbar>
          <Typography
            variant="h6"
            component="div"
            sx={{ textAlign: "center", maxWidth: "100%", width: "100%" }}
          >
            House Price Predictor
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}