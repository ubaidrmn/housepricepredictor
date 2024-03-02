# House Price Predictor

This application uses linear regression to predict house prices in Pakistan. It Considers the following features:
  - Area in marla
  - Bedrooms
  - Baths
  - Location
  - City
  - Property type

# Project Structure

| Directory/File      | Description                                            | URL                                             |
|---------------------|--------------------------------------------------------|-------------------------------------------------|
| `/api`              | Backend API built with FastAPI                         | [Backend API](http://localhost:8000/docs) |
| `/frontend`         | Frontend built with React.js                           | [Frontend](http://localhost:3000/) |

## Installation

### Using Docker

1. Make sure you have Docker installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Run `docker compose up` to build and start the containers.

### Manual Installation

#### Backend (API)

1. Navigate to the `api` directory.
2. Install the required Python packages by running:

`pip install -r requirements.txt`

3. Run the FastAPI server with:
   
`uvicorn main:app`

#### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages by running:

`npm install`

3. Start the React development server with:

`npm start`

## Usage

1. Once the project is running, open a web browser and navigate to the provided address (default is http://localhost:3000/).
2. Input the relevant features of the house including area, bedrooms, baths, location, city, and property type.
3. Click on the "Predict" button to generate the estimated house price.
