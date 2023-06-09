import React, { useEffect, useState } from 'react';

function MovieList() {
  const[movies, setMovies] = useState([]);

  const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';

  useEffect(() => {
    // Fetch movies from your Django backend
    fetch('http://127.0.0.1:8000')
      .then((response) => response.json())
      .then((data) => {
        // Parse the JSON string to get the movie objects
        const moviesData = JSON.parse(data.movies);
        setMovies(moviesData);
      })
      .catch((error) => console.log(error));
  }, []);

  return (
      <div className='grid-container'>
        {movies.map(movie => (
          <div key={movie.movie_id} className="grid-item">
            <img src={`${BASE_URL}${movie.poster_path}`} alt={movie.title} />
            <h2>{movie.title}</h2>
          </div>
        ))}
      </div>
  );
}

export default MovieList;
