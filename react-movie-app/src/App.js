import './App.css';
import React from 'react';
import ListMovies from './ListMovies';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import DisplayDetails from './DisplayDetails';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<ListMovies />} />
          <Route path="/movies/:movie_id" element={<DisplayDetails/>} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
