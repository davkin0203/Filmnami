import React, { useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import axios from 'axios';

function DisplayDetails() {
    const [movieDetails, setMovieDetails] = useState({});
    const {movie_id} = useParams();
    const BASE_URL = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/';

    useEffect(() => {
        fetchMovieDetails(movie_id);
    }, [movie_id]);
    
    const fetchMovieDetails = async (movie_id) => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/home/movies/movie-details/', {
                params: {
                    movie_id: movie_id,
                }
            });

            const movieDetails = JSON.parse(response.data.details);
            const movie = movieDetails[0];

            const movieData = {
                movie_id: movie.movie_id,
                title: movie.title,
                poster_path: movie.poster_path,
                overview: movie.overview,
                release_date: movie.release_date,
                runtime: movie.runtime,
                vote_average: movie.vote_average,
            };
                console.log(movieData);
                setMovieDetails(movieData);
            } catch(error) {
                console.error('Error fetching movie details ', error);
            }
    };

    return (
        <div className="movie-details-page">
            <div className="grid-item">
              {movieDetails.poster_path !== 'null' && <img src={`${BASE_URL}${movieDetails.poster_path}`} alt={movieDetails.title} />}
              {movieDetails.poster_path === 'null' && <img src={'https://content.schoolinsites.com/api/documents/ebbca81b01694c91aa908f5374842a9f.gif'} alt={movieDetails.title} />}
              <h2>{movieDetails.title}</h2>
              <h3>{movieDetails.runtime}</h3>
            </div>
        </div>
    )

}

export default DisplayDetails;