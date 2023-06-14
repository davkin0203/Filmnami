import React, { useEffect, useState } from 'react';
import Filter from './Filter';
import SearchBar from './SearchBar';

function ListMovies() {
  const[movies, setMovies] = useState([]);
  const [selectedFilter, setSelectedFilter] = useState('trending');
  const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';

  useEffect(() => {
    // Fetch movies from your Django backend
    fetchMovies();
  }, [selectedFilter]);

  const fetchMovies = () => {
    let url;

    if(selectedFilter === "popular") {
      url = 'http://127.0.0.1:8000/home/';
    } else {
      url = 'http://127.0.0.1:8000';
    }

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        // Parse the JSON string to get the movie objects
        const moviesData = JSON.parse(data.movies);
        setMovies(moviesData);
      })
      .catch((error) => console.log(error));
    };

    const handleFilterChange = (filter) => {
      setSelectedFilter(filter);
    };

    return (
      <div>
        <div className='grid-container-filter-search'>
          <div className='grid-child filter'>
            <Filter selectedFilter={selectedFilter} onFilterChange={handleFilterChange}/>
          </div>
          <div className='grid-child search'>
            <SearchBar/>
          </div>
        </div>
        <div className='grid-container'>
          {movies.map((movie) => (
            <div key={movie.id} className="grid-item">
              <img src={`${BASE_URL}${movie.poster_path}`} alt={movie.title} />
              <h2>{movie.title}</h2>
            </div>
          ))}
        </div>
      </div>
    );
  }
  
  export default ListMovies;