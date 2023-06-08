import React, { useEffect, useState } from 'react';

function MovieList() {
  const[movies, setMovies] = useState([]);

  useEffect(() => {
    // Fetch movies from your Django backend
    fetch('http://127.0.0.1:8000/movies/')
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
            <img src={movie.image_url} alt={movie.title} />
            <h2>{movie.title_text}</h2>
          </div>
        ))}
      </div>
  );
}

export default MovieList;
