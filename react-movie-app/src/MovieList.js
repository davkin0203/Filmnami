import { useEffect, useState } from 'react';

function MovieList() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    // Fetch movies from your Django backend
    fetch('movies/') // Replace with your Django API endpoint
      .then((response) => 
          response.json())
      .then((data) => 
          setMovies(data.movies))
      .catch((error) => 
          console.log(error));
  }, []);

  return (
    <div>
      <h1>Movies Listed!</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.movie_id}>
            <h2>{movie.title_text}</h2>
            <img src={movie.image_url} alt={movie.title_text} />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MovieList;
