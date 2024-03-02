import { Alert, Box, Button, Container, FormControl, InputLabel, MenuItem, Select, TextField, Typography } from '@mui/material';
import { useEffect, useState } from 'react';
import converter from "number-to-words";
import Navbar from './Navbar';


function App() {
  // Features
  const [city, setCity] = useState("Loading..");
  const [location, setLocation] = useState("Loading..");
  const [propertyType, setPropertyType] = useState("Loading..");
  const [bedrooms, setBedrooms] = useState("");
  const [area, setArea] = useState("");
  const [baths, setBaths] = useState("");

  // Fetch data
  const [categoricalFeatures, setCategoricalFeatures] = useState(null);
  const [currentLocations, setCurrentLocations] = useState(null);
  const [predictedPrice, setPredictedPrice] = useState(null);
  const API_URL = process.env.API_URL || "http://localhost:8000";

  async function loadCategoricalFeatures() {
    const res = await fetch(`${API_URL}/categorical-features`);
    const data = await res.json();
    console.log(data)
    setCity(data.cities[0]);
    setPropertyType(data.property_types[0]);
    setCategoricalFeatures(data);
  }

  async function predictPrice() {
    const body = {
      "property_type": propertyType,
      "location": location,
      "city": city,
      "baths": baths,
      "bedrooms": bedrooms,
      "area_marla": area
    }

    const res = await fetch(`${API_URL}/predict`, {
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body),
      method: "POST"
    });

    const data = await res.json();

    setPredictedPrice(data.price)
  }

  useEffect(() => { loadCategoricalFeatures(); }, [])

  useEffect(() => {
    if (city && categoricalFeatures) {
      setCurrentLocations(categoricalFeatures.locations[city]);
      setLocation(categoricalFeatures.locations[city][0]);
    }
  }, [city])

  return (
    <>
      <Navbar />
      <Container sx={{
        display: "flex",
        flexDirection: "row",
        justifyContent: "center",
        marginTop: "50px"
      }}>
        <Box sx={{
          maxWidth: "600px",
          width: "100%",
          marginTop: "50px",
          display: "flex",
          flexDirection: "column",
          rowGap: "20px"
        }}>
          <FormControl sx={{
            maxWidth: "100%",
            width: "100%"
          }}>
            <InputLabel shrink>
              City
            </InputLabel>
            <Select
              value={city}
              onChange={e => setCity(e.target.value)}
            >
              {categoricalFeatures && categoricalFeatures.cities.map(value => {
                return <MenuItem key={value} value={value}>{value}</MenuItem>
              })}
            </Select>
          </FormControl>

          <FormControl sx={{
            maxWidth: "100%",
            width: "100%"
          }}>
            <InputLabel shrink>
              Location
            </InputLabel>
            <Select
              value={location}
              onChange={e => setLocation(e.target.value)}
            >
              {currentLocations && currentLocations.map(value => {
                return <MenuItem key={value} value={value}>{value}</MenuItem>
              })}
            </Select>
          </FormControl>

          <FormControl sx={{
            maxWidth: "100%",
            width: "100%"
          }}>
            <InputLabel shrink>
              Property Type
            </InputLabel>
            <Select
              value={propertyType}
              onChange={e => setLocation(e.target.value)}
            >
              {categoricalFeatures && categoricalFeatures.property_types.map(value => {
                return <MenuItem key={value} value={value}>{value}</MenuItem>
              })}
            </Select>
          </FormControl>

          <TextField type="number" onChange={e => setArea(e.target.value)} value={area} label="Area (Marla)" variant="outlined" />
          <TextField type="number" onChange={e => setBedrooms(e.target.value)} value={bedrooms} label="No. of Bedrooms" variant="outlined" />
          <TextField type="number" onChange={e => setBaths(e.target.value)} value={baths} label="No. of Baths" variant="outlined" />

          <Button onClick={predictPrice} variant={"contained"}>Predict Price</Button>

          {predictedPrice && 
          <Alert variant="filled" severity="success">
            Prediction: {converter.toWords(predictedPrice)} PKR
          </Alert>}
        </Box>
      </Container>
    </>
  );
}

export default App;
